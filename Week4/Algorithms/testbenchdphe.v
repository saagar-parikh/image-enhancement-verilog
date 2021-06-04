`timescale 1ns / 1ps

module testbench();

    parameter size = 28500;                     // Size of image = 28500 = 190 x 150
    reg [7:0] init_2D_img [0:size-1];           // Memory to store 8-bit data image
    wire [7:0] final_2D_img [0:size-1];         // Memory to store final 8-bit image
    wire [size*8 - 1: 0] init_img;              // Initial image 1D array
    wire [size*8 - 1: 0] final_img;             // Final image 1D array
    integer i,f;
    
    dphe Instance(init_img, final_img);
    
    initial begin
        #10
        $readmemb("C:\\Users\\dmp\\Downloads\\4119_binary_190x150.txt", init_2D_img); // read image file
      
        #10
        f = $fopen("dphe_output2.txt","w");             // Open file to read image
        #10
        for (i = 0; i<size; i=i+1) begin    
            $fwrite(f,"%b\n",final_2D_img[i]);          // Write final image into text file line by line
        end
    
        #10;
        $fclose(f);                                     // Close file
        
        
    end

    genvar j;
    // Convert initial 2D image array into 1D array
    generate
        for (j=0; j<size; j=j+1) begin
            assign init_img[8*j + 7 : 8*j] = init_2D_img[j];
        end
    endgenerate
    
    // Convert final image 1D array into 2D array tobe writteninthe file
    generate
        for (j=0; j<size; j=j+1) begin
            assign final_2D_img[j] = final_img[8*j + 7 : 8*j];
        end
    endgenerate
    
endmodule