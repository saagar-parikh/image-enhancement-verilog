`timescale 1ns / 1ps


module dphe(init_img, final_img);
    input [28500*8 - 1:0] init_img;
    output [28500*8 - 1:0] final_img;
        
    parameter size = 28500;                         // Size of image = 28500 = 190 x 150
    wire [7:0] init_img_2d [0:size-1];              // Store initial image in 2D array
    reg [7:0] final_img_2d [0:size-1];              // Store final image in 2D array
    
    // Grayscale values having frequencies < Tup and > Tdown and =0 will be stored in this array
    reg[7:0]to_add[0:size-1];
    // Grayscale values having frequencies < Tup and > Tdown will be stored from this array                  
    reg[7:0]to_subtract[0:size-1];
    
    reg [15:0] origfreq [0:255];                    // Store original frequencies of grayscale values
    reg [15:0] newfreq [0:255];                     // Store final frequencies of grayscale values
    reg [15:0] newgrayval [0:255];                  // Store new grayscale values
    integer i,l,count1,count2;                      // Used as indexes in loops
    integer g1,g2;                                  // Temp variables used for storing grayscale values inside for loop
    integer excess,deficit;                         // Number of excess, deficit pixels after clipping
    integer Tup,Tdown;                              // Upper, lower thresholds
    integer count,total,not_zero;                   // Used a to calculate upper threshold frequency
    
    initial begin
        
        // Initialize arrays to 0
        for (i=0; i<256; i=i+1) begin
            origfreq[i]=16'b0000000000000000;
            newgrayval[i]=16'b0000000000000000;
        end
        
        // Initialize arrays to 0
        for (i=0; i<size; i=i+1) begin
            to_add[i]=8'b00000000;
            to_subtract[i]=8'b00000000;
        end
        
        //Initialize variables to 0
        excess=0;
        deficit=0;
        not_zero=0;
        Tup=0;
        Tdown=0;
        total=0;
        count=0;
    end
    
  genvar j;
  
  // Writing the 1D image array into the 2D image array
  generate
    for (j=0; j<size; j=j+1) begin
         assign init_img_2d[j]= init_img[8*j + 7 : 8*j];
    end
  endgenerate

    always@(*) begin
        
        // Calculate original frequencies
        for (i=0;i<size;i=i+1) begin
            g1=init_img_2d[i];
            origfreq[g1]=origfreq[g1]+1;
        end
        
        // Calculate average of all local maxima (except those adjacent to 0) for Tup
        for (i=0;i<256;i=i+1) begin
            if (origfreq[i]!=0)
                not_zero=not_zero+1;
            if ((i<255) && (i>=1) && ((origfreq[i+1]>0) || (origfreq[i-1]>0))) begin
                if ((origfreq[i]>origfreq[i+1]) || (origfreq[i]>origfreq[i-1])) begin
                    count=count+1;
                    total=total+origfreq[i];
                end
            end
        end
        Tup=total/count;                            // Upper threshold frequency
        
        // Calculate Tdown from Tup
        if ((not_zero*Tup)>size)
            Tdown=size/255;
        else 
            Tdown=not_zero*Tup/255;
            
        $display("Tup = %d, Tdown = %d",Tup,Tdown); // Display the upper and lower thresholds
        
        // Clipping of the histogram
        for (i=0;i<256;i=i+1) begin                 
            if (origfreq[i]==0) begin               // For graysale values having 0 frequency, 
                newfreq[i]=origfreq[i];             // new frequencies will remain same
                to_add[count1]=i;                   // Store these grayscale values in to_add
                count1=count1+1;                    // Change the index of to_add
            end
            else if (origfreq[i]<Tdown) begin       // For grayscale values having frequencies < Tdown,
                deficit=deficit+Tdown-origfreq[i];  // bump them up to Tdown
                newfreq[i]=Tdown;
            end
            else if(origfreq[i]<Tup) begin          // For grayscale values having frequencies between both thresholds,
                newfreq[i]=origfreq[i];             // new frequencies will remain same
                to_add[count1]=i;                   // Store these grayscale values in to_add
                count1=count1+1;                    // Change the index of to_add
                to_subtract[count2]=i;              // Store these grayscale values in to_subtract
                count2=count2+1;                    // Change the index of to_subtract
            end
            else begin                              // For grayscale values having frequencies > Tup,
                excess=excess+origfreq[i]-Tup;      // clip them down to Tup
                newfreq[i]=Tup;
            end
        end
        
        // Redistribute excess pixels into other bins
        for (i=0;i<count1;i=i+1) begin
            if ((newfreq[to_add[i]]+(excess/count1))<Tup)
                newfreq[to_add[i]]=newfreq[to_add[i]]+(excess/count1);
        end
        
        // Redistribute deficit pixels into other bins
        for (i=0;i<count2;i=i+1) begin
            if ((newfreq[to_subtract[i]]-(deficit/count2))>Tdown)
                newfreq[to_subtract[i]]=newfreq[to_subtract[i]]-(deficit/count2);
        end
        
        // Histogram equalization
        for (i=0;i<256;i=i+1) begin
            for (l=0;l<=i;l=l+1) begin
              newgrayval[i] = newgrayval[i] + newfreq[l];
            end
            newgrayval[i] =(newgrayval[i] * 255)/size;
        end
        
        // Remapping the final frequencies onto the image
        for (i=0;i<size;i=i+1) begin
            g2=init_img_2d[i];
            final_img_2d[i]=newgrayval[g2];
        end
                
    end
    
    // Converting the final 2D image array back into 1D image array
    generate
        for (j=0; j<size; j=j+1) begin
            assign final_img[8*j + 7 : 8*j] = final_img_2d[j];
        end
    endgenerate

endmodule