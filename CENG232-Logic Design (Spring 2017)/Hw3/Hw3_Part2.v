`timescale 1ns / 1ps 
module lab3_2(
			input[4:0] word,
			input CLK, 
			input selection,
			input mode,
			output reg [7:0] hipsterians1,
			output reg [7:0] hipsterians0,
			output reg [7:0] nerdians1,
			output reg [7:0] nerdians0,
			output reg warning
    );
	 

	initial begin
		hipsterians0=0;
		nerdians0=0;
		hipsterians1=0;
		nerdians1=0;
		warning=0;
	end
	
	integer crop = 999;
	
	always @(posedge CLK)
	begin

		warning <= 0;
		
		/*
		if(mode==1 && selection==1 && (word[1:0]==3))
		begin
			nerdians1 <= nerdians1 + 1;
		end
		else begin
			hipsterians0 <= hipsterians0 + 1;
		end
		*/
		
		//Increase and Decrease Cases
		if((selection==0 && mode==0)&&(word[4:3]==0 || word[3:2]==0 || word[2:1]==0 || word[1:0]==0))
		begin
			//DECREASE HIPSTERIANS
			if(hipsterians0==0 && hipsterians1==0)
			begin
					crop <= crop-1;
			end
			else if(hipsterians0==0 && (hipsterians1==1 || hipsterians1==2))
			begin
				hipsterians1 <= hipsterians1 - 1;
				hipsterians0 <= 9;
			end
			else if(hipsterians0!=0 && (hipsterians1==0 || hipsterians1==1))
			begin
				hipsterians0 <= hipsterians0 - 1;
			end
		end
		
		else if((selection==0 && mode==1)&&(word[4:3]==0 || word[3:2]==0 || word[2:1]==0 || word[1:0]==0))
		begin
			//INCREASE HIPSTERIANS
			if(hipsterians1==2 && hipsterians0==0)
			begin
				hipsterians1 <=0;
			end
			else if(hipsterians0==9 && (hipsterians1==0 || hipsterians1==1))
			begin
				hipsterians1 <= hipsterians1 + 1;
				hipsterians0 <= 0;
			end
			else if((hipsterians1==0 || hipsterians1==1) && hipsterians0!=9)
			begin
				hipsterians0 <= hipsterians0 + 1;
			end
		end
		
		else if((selection==1 && mode==0)&&(word[4:3]==3 || word[3:2]==3 || word[2:1]==3 || word[1:0]==3))
		begin
			//DECREASE NERDIANS
			if(nerdians0==0 && nerdians1==0)
			begin
					crop <= crop-1;
			end
			else if(nerdians0==0 && (nerdians1==1 || nerdians1==2))
			begin
				nerdians1 <= nerdians1 - 1;
				nerdians0 <= 9;
			end
			else if(nerdians0!=0 && (nerdians1==0 || nerdians1==1))
			begin
				nerdians0 <= nerdians0 - 1;
			end
		end
		
		else if((selection==1 && mode==1)&&(word[4:3]==3 || word[3:2]==3 || word[2:1]==3 || word[1:0]==3))
		begin
			//INCREASE NERDANS
			if(nerdians1 == 0 && nerdians0 == 0)
			begin
				nerdians0 <= nerdians0 + 1;
			end
			else if((nerdians1 == 0 || nerdians1 == 1) && nerdians0 == 9)
			begin
				nerdians1 <= nerdians1 + 1;
				nerdians0 <= 0;
			end
			else if(nerdians1 == 2 && nerdians0 == 0)
			begin
				nerdians1 <= 0;
			end
			else if((nerdians1 == 1 || nerdians1 == 0) && nerdians0 != 9)
			begin
				nerdians0 <= nerdians0 + 1;
			end
		end
		
		//Both Cases
		else if((selection==0 && mode==0)&&(word[4:3]==0 || word[3:2]==0 || word[2:1]==0 || word[1:0]==0)&&(word[4:3]==3 || word[3:2]==3 || word[2:1]==3 || word[1:0]==3))
		begin
			//DECREASE HIPSTERIANS
			if(hipsterians0==0 && hipsterians1==0)
			begin
					crop <= crop-1;
			end
			else if(hipsterians0==0 && (hipsterians1==1 || hipsterians1==2))
			begin
				hipsterians1 <= hipsterians1 - 1;
				hipsterians0 <= 9;
			end
			else if(hipsterians0!=0 && (hipsterians1==0 || hipsterians1==1))
			begin
				hipsterians0 <= hipsterians0 - 1;
			end
		end
		
		else if((selection==0 && mode==1)&&(word[4:3]==0 || word[3:2]==0 || word[2:1]==0 || word[1:0]==0)&&(word[4:3]==3 || word[3:2]==3 || word[2:1]==3 || word[1:0]==3))
		begin
			//INCREASE HIPSTERIANS
			if(hipsterians1==2 && hipsterians0==0)
			begin
				hipsterians1 <=0;
			end
			else if(hipsterians0==9 && (hipsterians1==0 || hipsterians1==1))
			begin
				hipsterians1 <= hipsterians1 + 1;
				hipsterians0 <= 0;
			end
			else if((hipsterians1==0 || hipsterians1==1) && hipsterians0!=9)
			begin
				hipsterians0 <= hipsterians0 + 1;
			end
		end
		
		else if((selection==1 && mode==0)&&(word[4:3]==3 || word[3:2]==3 || word[2:1]==3 || word[1:0]=={1,1})&&(word[4:3]==0 || word[3:2]==0 || word[2:1]==0 || word[1:0]==0))
		begin
			//DECREASE NERDIANS
			if(nerdians0==0 && nerdians1==0)
			begin
					crop <= crop-1;
			end
			else if(nerdians0==0 && (nerdians1==1 || nerdians1==2))
			begin
				nerdians1 <= nerdians1 - 1;
				nerdians0 <= 9;
			end
			else if(nerdians0!=0 && (nerdians1==0 || nerdians1==1))
			begin
				nerdians0 <= nerdians0 - 1;
			end
		end
		
		else if((selection==1 && mode==1)&&(word[4:3]==3 || word[3:2]==3 || word[2:1]==3 || word[1:0]==3)&&(word[4:3]==0 || word[3:2]==0 || word[2:1]==0 || word[1:0]==0))
		begin
			//INCREASE NERDIANS
			if(nerdians1 == 0 && nerdians0 == 0)
			begin
				nerdians0 <= nerdians0 + 1;
			end
			else if((nerdians1 == 0 || nerdians1 == 1) && nerdians0 == 9)
			begin
				nerdians1 <= nerdians1 + 1;
				nerdians0 <= 0;
			end
			else if(nerdians1 == 2 && nerdians0 == 0)
			begin
				nerdians1 <= 0;
			end
			else if((nerdians1 == 1 || nerdians1 == 0) && nerdians0 != 9)
			begin
				nerdians0 <= nerdians0 + 1;
			end
		end
		
		//Warnings
		else if(selection==0 && (mode==1 || mode==0) && (word[4:3]==3 || word[3:2]==3 || word[2:1]==3 || word[1:0]==3) && (word[4:3]!=0 && word[3:2]!=0 && word[2:1]!=0 && word[1:0]!=0))
		begin
			//WARNING
			warning <=1;
		end
		else if(selection==1 && (mode==1 || mode==0) && (word[4:3]!=3 && word[3:2]!=3 && word[2:1]!=3 && word[1:0]!=3) && (word[4:3]==0 || word[3:2]==0 || word[2:1]==0 || word[1:0]==0))
		begin
			//WARNING
			warning<=1;
		end
		else if((word[4:3]!=3 && word[3:2]!=3 && word[2:1]!=3 && word[1:0]!=3) && (word[4:3]!=0 && word[3:2]!=0 && word[2:1]!=0 && word[1:0]!=0))
		begin
			//WARNING
			warning<=1;
		end
	end
	
endmodule
