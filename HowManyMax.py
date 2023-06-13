t = int(input("Enter no. of test cses = ")) 
for i in range(t):
    n = int(input())
    s = input()
    clk = 0
    if (s[0]=="1"):
        clk = clk + 1
    if(s[-1] == "0"):
        clk = clk + 1
    k = s.count("01")
    
    clk = clk +1
    print(clk)        
        
        
    
    
    
    
    
    
    