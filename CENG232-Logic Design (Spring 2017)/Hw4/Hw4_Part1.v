`timescale 1ns / 1ps
module FUNCROM (input [3:0] romAddress, output reg[4:0] romData);
	
always@(romAddress)
begin
		case(romAddress)
			4'b0000: romData = 0;
			4'b0001: romData = 2;
			4'b0010: romData = 4;
			4'b0011: romData = 7;
			4'b0100: romData = 10;
			4'b0101: romData = 11;
			4'b0110: romData = 13;
			4'b0111: romData = 14;
			4'b1000: romData = 17;
			4'b1001: romData = 18;
			4'b1010: romData = 20;
			4'b1011: romData = 23;
			4'b1100: romData = 25;
			4'b1101: romData = 26;
			4'b1110: romData = 30;
			4'b1111: romData = 31;
		endcase
	end
endmodule
																						
module FUNCRAM (input mode,input [3:0] ramAddress, input [4:0] dataIn,input op, input [1:0] arg,  input CLK, output reg [8:0] dataOut);

reg [8:0]registerz[15:0];
	
	initial begin
		registerz[0] = 9'b000000000;
		registerz[1] = 9'b000000000;
		registerz[2] = 9'b000000000;
		registerz[3] = 9'b000000000;
		registerz[4] = 9'b000000000;
		registerz[5] = 9'b000000000;
		registerz[6] = 9'b000000000;
		registerz[7] = 9'b000000000;
		registerz[8] = 9'b000000000;
		registerz[9] = 9'b000000000;
		registerz[10] = 9'b000000000;
		registerz[11] = 9'b000000000;
		registerz[12] = 9'b000000000;
		registerz[13] = 9'b000000000;
		registerz[14] = 9'b000000000;
		registerz[15] = 9'b000000000;
	end
	
integer sum;
integer x;
integer temp;

always@(posedge CLK)begin
	if(mode==1) begin //Write mode is active:
			case(arg)
				2'b00: x = 2;
				2'b01: x = 1;
				2'b10: x = -1;
				2'b11: x = -2;
			endcase
		if(op==0)begin //Modulus 7 operation will be performed:
			case(ramAddress)
				4'b0000:begin
					sum =((x*x*x*x)+(x*x*x)+(x*x)+(x)+1)%7;
					if(sum<0)sum=sum+7;
					registerz[0][8:0] = sum;
					dataOut = registerz[0];
				end
				4'b0001:begin
					sum =((x*x*x*x)+(x*x*x)+(x*x)-(x)+1)%7;
					if(sum<0)sum=sum+7;
					registerz[1] = sum;
					dataOut = registerz[1];
				end
				4'b0010:begin
					sum =((x*x*x*x)+(x*x*x)-(x*x)+(x)+1)%7;
					if(sum<0)sum=sum+7;
					registerz[2] = sum;
					dataOut = registerz[2];
				end
				4'b0011:begin
					sum =((x*x*x*x)+(x*x*x)-(x*x)-(x)-1)%7;
					if(sum<0)sum=sum+7;
					registerz[3] = sum;
					dataOut = registerz[3];
				end
				4'b0100:begin
					sum =((x*x*x*x)-(x*x*x)+(x*x)-(x)+1)%7;
					if(sum<0)sum=sum+7;
					registerz[4] = sum;
					dataOut = registerz[4];
				end
				4'b0101:begin
					sum =((x*x*x*x)-(x*x*x)+(x*x)-(x)-1)%7;
					if(sum<0)sum=sum+7;
					registerz[5] = sum;
					dataOut = registerz[5];
				end
				4'b0110:begin
					sum =((x*x*x*x)-(x*x*x)-(x*x)+(x)-1)%7;
					if(sum<0)sum=sum+7;
					registerz[6] = sum;
					dataOut = registerz[6];
				end
				4'b0111:begin
					sum =((x*x*x*x)-(x*x*x)-(x*x)-(x)+1)%7;
					if(sum<0)sum=sum+7;
					registerz[7] = sum;
					dataOut = registerz[7];
				end
				4'b1000:begin
					sum =(-(x*x*x*x)+(x*x*x)+(x*x)+(x)-1)%7;
					if(sum<0)sum=sum+7;
					registerz[8] = sum;
					dataOut = registerz[8];
				end
				4'b1001:begin
					sum =(-(x*x*x*x)+(x*x*x)+(x*x)-(x)+1)%7;
					if(sum<0)sum=sum+7;
					registerz[9] = sum;
					dataOut = registerz[9];
				end
				4'b1010:begin
					sum =(-(x*x*x*x)+(x*x*x)-(x*x)+(x)+1)%7;
					if(sum<0)sum=sum+7;
					registerz[10] = sum;
					dataOut = registerz[10];
				end
				4'b1011:begin
					sum =(-(x*x*x*x)+(x*x*x)-(x*x)-(x)-1)%7;
					if(sum<0)sum=sum+7;
					registerz[11] = sum;
					dataOut = registerz[11];
				end
				4'b1100:begin
					sum =(-(x*x*x*x)-(x*x*x)+(x*x)+(x)-1)%7;
					if(sum<0)sum=sum+7;
					registerz[12] = sum;
					dataOut = registerz[12];
				end
				4'b1101:begin
					sum =(-(x*x*x*x)-(x*x*x)+(x*x)-(x)+1)%7;
					if(sum<0)sum<=sum+7;
					registerz[13] = sum;
					dataOut = registerz[13];
				end
				4'b1110:begin
					sum =(-(x*x*x*x)-(x*x*x)-(x*x)-(x)+1)%7;
					if(sum<0)sum=sum+7;
					registerz[14] = sum;
					dataOut = registerz[14];
				end
				4'b1111:begin
					sum =(-(x*x*x*x)-(x*x*x)-(x*x)-(x)-1)%7;
					if(sum<0)sum=sum+7;
					registerz[15] = sum;
					dataOut = registerz[15];
				end
			endcase
		end
		else if(op == 1) begin //Derivative operation will be performed:
			case(ramAddress)
				4'b0000:begin
					sum = 4*(x*x*x)+3*(x*x)+2*x+1;
					if(sum<0)begin
						registerz[0][8] = 1;
						registerz[0][7:0] = -sum;
					end
					else begin
						registerz[0][8] = 0;
						registerz[0][7:0] = sum;
					end
					dataOut = registerz[0];
				end
				4'b0001:begin
					sum =4*(x*x*x)+3*(x*x)+2*x-1;
					if(sum<0)begin
						registerz[1][8] = 1;
						registerz[1][7:0] = -sum;
					end
					else begin
						registerz[1][8] = 0;
						registerz[1][7:0] = sum;
					end
					dataOut = registerz[1];
				end
				4'b0010:begin
					sum =4*(x*x*x)+3*(x*x)-2*x+1;
					if(sum<0)begin
						registerz[2][8] = 1;
						registerz[2][7:0] = -sum;
					end
					else begin
						registerz[2][8] = 0;
						registerz[2][7:0] = sum;
					end
					dataOut = registerz[2];
				end
				4'b0011:begin
					sum =4*(x*x*x)+3*(x*x)-2*x-1;
					if(sum<0)begin
						registerz[3][8] = 1;
						registerz[3][7:0] = -sum;
					end
					else begin
						registerz[3][8] = 0;
						registerz[3][7:0] = sum;
					end
					dataOut = registerz[3];
				end
				4'b0100:begin
					sum =4*(x*x*x)-3*(x*x)+2*x-1;
					if(sum<0)begin
						registerz[4][8] = 1;
						registerz[4][7:0] = -sum;
					end
					else begin
						registerz[4][8] = 0;
						registerz[4][7:0] = sum;
					end
					dataOut = registerz[4];
				end
				4'b0101:begin
					sum =4*(x*x*x)-3*(x*x)+2*x-1;
					if(sum<0)begin
						registerz[5][8] = 1;
						registerz[5][7:0] = -sum;
					end
					else begin
						registerz[5][8] = 0;
						registerz[5][7:0] = sum;
					end
					dataOut = registerz[5];
				end
				4'b0110:begin
					sum =4*(x*x*x)-3*(x*x)-2*x+1;
					if(sum<0)begin
						registerz[6][8] = 1;
						registerz[6][7:0] = -sum;
					end
					else begin
						registerz[6][8] = 0;
						registerz[6][7:0] = sum;
					end
					dataOut = registerz[6];
				end
				4'b0111:begin
					sum =4*(x*x*x)-3*(x*x)-2*x-1;
					if(sum<0)begin
						registerz[7][8] = 1;
						registerz[7][7:0] = -sum;
					end
					else begin
						registerz[7][8] = 0;
						registerz[7][7:0] = sum;
					end
					dataOut = registerz[7];
				end
				4'b1000:begin
					sum =-4*(x*x*x)+3*(x*x)+2*x+1;
					if(sum<0)begin
						registerz[8][8] = 1;
						registerz[8][7:0] = -sum;
					end
					else begin
						registerz[8][8] = 0;
						registerz[8][7:0] = sum;
					end
					dataOut = registerz[8];
				end
				4'b1001:begin
					sum =-4*(x*x*x)+3*(x*x)+2*x-1;
					if(sum<0)begin
						registerz[9][8] = 1;
						registerz[9][7:0] = -sum;
					end
					else begin
						registerz[9][8] = 0;
						registerz[9][7:0] = sum;
					end
					dataOut = registerz[9];
				end
				4'b1010:begin
					sum =-4*(x*x*x)+3*(x*x)-2*x+1;
					if(sum<0)begin
						registerz[10][8] = 1;
						registerz[10][7:0] = -sum;
					end
					else begin
						registerz[10][8] = 0;
						registerz[10][7:0] = sum;
					end
					dataOut = registerz[10];
				end
				4'b1011:begin
					sum =-4*(x*x*x)+3*(x*x)-2*x-1;
					if(sum<0)begin
						registerz[11][8] = 1;
						registerz[11][7:0] = -sum;
					end
					else begin
						registerz[11][8] = 0;
						registerz[11][7:0] = sum;
					end
					dataOut = registerz[11];
				end
				4'b1100:begin
					sum =-4*(x*x*x)-3*(x*x)+2*x+1;
					if(sum<0)begin
						registerz[12][8] = 1;
						registerz[12][7:0] = -sum;
					end
					else begin
						registerz[12][8] = 0;
						registerz[12][7:0] = sum;
					end
					dataOut = registerz[12];
				end
				4'b1101:begin
					sum =-4*(x*x*x)-3*(x*x)+2*x-1;
					if(sum<0)begin
						registerz[13][8] = 1;
						registerz[13][7:0] = -sum;
					end
					else begin
						registerz[13][8] = 0;
						registerz[13][7:0] = sum;
					end
					dataOut = registerz[13];
				end
				4'b1110:begin
					sum =-4*(x*x*x)-3*(x*x)-2*x-1;
					if(sum<0)begin
						registerz[14][8] = 1;
						registerz[14][7:0] = -sum;
					end
					else begin
						registerz[14][8] = 0;
						registerz[14][7:0] = sum;
					end
					dataOut = registerz[14];
				end
				4'b1111:begin
					sum =-4*(x*x*x)-3*(x*x)-2*x-1;
					if(sum<0)begin
						registerz[15][8] = 1;
						registerz[15][7:0] = -sum;
					end
					else begin
						registerz[15][8] = 0;
						registerz[15][7:0] = sum;
					end
					dataOut = registerz[15];
				end
			endcase
		end
	end
end
always@(ramAddress,op,arg,mode,dataIn)begin
	if(mode==0)begin
		case(ramAddress)
			4'b0000: dataOut = registerz[0];
			4'b0001: dataOut = registerz[1];
			4'b0010: dataOut = registerz[2];
			4'b0011: dataOut = registerz[3];
			4'b0100: dataOut = registerz[4];
			4'b0101: dataOut = registerz[5];
			4'b0110: dataOut = registerz[6];
			4'b0111: dataOut = registerz[7];
			4'b1000: dataOut = registerz[8];
			4'b1001: dataOut = registerz[9];
			4'b1010: dataOut = registerz[10];
			4'b1011: dataOut = registerz[11];
			4'b1100: dataOut = registerz[12];
			4'b1101: dataOut = registerz[13];
			4'b1110: dataOut = registerz[14];
			4'b1111: dataOut = registerz[15];
		endcase
	end
end

endmodule


module FUNCMEMORY(input mode, input [6:0] memInput, input CLK, output wire [8:0] result);
	/*Don't edit this module*/
	wire [4:0]  romData;

	FUNCROM RO(memInput[6:3], romData);
	FUNCRAM RA(mode, memInput[6:3], romData, memInput[2],memInput[1:0], CLK, result);

endmodule
