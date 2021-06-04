`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 02.11.2020 17:40:42
// Design Name: 
// Module Name: testbench
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module testbench();
parameter HEIGHT=256;
parameter WIDTH=324;
//parameter INFILE="C:\\Users\\dmp\\Downloads\\4119_binary.txt";
parameter sizeOfLengthReal = 82944;
reg [7:0] total_memory [0:sizeOfLengthReal-1];// memory to store  8-bit data image
//reg start=1'b1;
//integer temp_BMP   [0 : WIDTH*HEIGHT - 1]; // temporary memory to save image data : size will be WIDTH*HEIGHT*3
integer i;

initial begin
    #10
    $readmemb("C:\\Users\\dmp\\Downloads\\4119_binary.txt", total_memory); // read file from INFILE
    
    #100
    
    for (i=0; i<sizeOfLengthReal-1;i=i+1) begin
        $display("%b",total_memory[i]);#1;
    end
    #10;
    $finish;
    /*if(start == 1'b1) begin
        for(i=0; i<WIDTH*HEIGHT ; i=i+1) begin
            temp_BMP[i] = total_memory[i+0][7:0]; 
        end
        
        for(i=0; i<HEIGHT; i=i+1) begin
            for(j=0; j<WIDTH; j=j+1) begin
                
            end
        end
    end*/
end

endmodule
