def next_palindrome(base):
    
    check = False
    l = len( base )
    half = int(l/2)
    
    if l % 2 == 1:
        for i in range(half+1):
            if base[ half-i ] > base[ half + i ]:
                check = True
                break
            elif base[ half-i ] <= base[ half + i ]:
                check = False
                break
        if check:
            print("Left > Right")
            for i in range(half+1):
                base[ half + i ] = base[ half - i ]
        else:
            print("Left <= Right")
            for i in range(half+1):
                if base[half-i] == '9':
                    
                    
            
        
        
n = int( input() )        

for i in range(n):
    base = list( input() )
    next_palin = next_palindrome( base )
    

    print( next_palin )
