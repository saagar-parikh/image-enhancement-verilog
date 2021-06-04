`timescale 1ns / 1ps

module HistEqual(init_img, final_img);
    input [28500*8 - 1:0] init_img;     //1D array of initial image
    output [28500*8 - 1:0] final_img;   //1D array of final image
    
    parameter size = 28500;
    wire[7:0]init_img_2d[0:size-1];     //Store the initial image in a 2D array
    reg [7:0] final_img_2d [0:size-1];  //Store the final image(equalized) in a 2D array
    
    reg [15:0] origfreq [0:255];        //Store the original frequencies of each grayscale value
    reg [15:0] newgrayval [0:255];      //Store the final grayscale values
    integer i,g1,g2;
    
    initial begin
    
        for (i=0; i<256; i=i+1) begin               //Initialize the arrays
            origfreq[i]=16'b0000000000000000;
            newgrayval[i]=16'b0000000000000000;
        end
    
    end
    
    genvar j;
    
    // writing the 1d initial image into the 2d image
    generate
      for (j=0; j<size; j=j+1) begin
           assign init_img_2d[j]= init_img[8*j + 7 : 8*j];
      end
    endgenerate

    always@(*) begin
        
        //for loop to count frequency of grayscale values
        for (i=0;i<size;i=i+1) begin                
            g1=init_img_2d[i];
            origfreq[g1]=origfreq[g1]+1;
            $display("g1 = %d, i = %d",g1,i);
        end
        
        //for loop to calculate final grayscale values
        for (i=0;i<256;i=i+1) begin
            for (i=0;i<=i;i=i+1) begin
              newgrayval[i] = newgrayval[i] + origfreq[i];
            end
            newgrayval[i] =(newgrayval[i] * 255)/size;
        end
        
        //Re-map values from equalized histogram into the image
        for (i=0;i<size;i=i+1) begin
            g2=init_img_2d[i];
            final_img_2d[i]=newgrayval[g2];
        end
                
    end
    
    //Converting the final 2D image into 1D array
    generate
        for (j=0; j<size; j=j+1) begin
            assign final_img[8*j + 7 : 8*j] = final_img_2d[j];
        end
    endgenerate

endmodule