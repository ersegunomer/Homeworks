`timescale 1ns / 1ps

module af(
    input a,
    input f,
    input clk,
    output reg q
    );
	 
    initial begin
        q = 0;
    end
	
    always@(posedge clk)
	 begin
		if(a==0 && f==0)
			q <= ~q;
		else if(a==0 && f==1)
			q <= q;
		else if(a==1 && f==0)
			q <= 1;
		else if(a==1 && f==1)
			q <= 0;
	 end

endmodule


module ic1500(
    input a0, 
    input f0, 
    input a1, 
    input f1, 
    input clk, 
    output q0, 
    output q1, 
    output y
    );
    
	 af afust(
		.a		(a0),
		.f		(f0),
		.clk	(clk),
		.q		(q0)
	 );
	 
	 af afalt(
		.a		(a1),
		.f		(f1),
		.clk	(clk),
		.q		(q1)
	 );
	 
	 assign y = q0 ~^ q1;
	 
	
endmodule
