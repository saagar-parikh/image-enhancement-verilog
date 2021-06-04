`timescale 1ns / 1ps


module testbench();
    parameter size = 28500;
    reg [7:0] initial_2D_img [0:size-1];            // memory to store 8-bit data image
    wire [7:0] final_2D_img [0:size-1];             // memory to store 8-bit final image
    wire [size*8 - 1: 0] init_img;                  // 1D array for initial image
    wire [size*8 - 1: 0] final_img;                 // 1D array for final image
    integer i,f;
    
    HistEqual Instance(init_img, final_img);
    
    initial begin
        #10
        $readmemb("C:\\Users\\acer\\Downloads\\4119_binary_190x150.txt", initial_2D_img); 	// read image file
      
        #10
        f = $fopen("4119_he_vivado.txt","w");	   // Open file to write final image
        
        #10
        for (i = 0; i<size; i=i+1) begin
          $fwrite(f,"%b\n",final_2D_img[i]);  	   // Write the final image 1D array line by line
        end
        
        #10;
        $fclose(f); 				   // Close file

    end
    
    genvar j;
    // Convert initial 2D image into 1D array (flattening)
    generate
        for (j=0; j<size; j=j+1) begin
            assign init_img[8*j + 7 : 8*j] = initial_2D_img[j];
        end
    endgenerate
    
    // Convert 1D array of final image into 2D image
    generate
        for (j=0; j<size; j=j+1) begin
            assign final_2D_img[j] = final_img[8*j + 7 : 8*j];
        end
    endgenerate
    
endmodule