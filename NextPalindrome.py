def next_palindrome( string ):
    l = len( string )
    half = int(l/2)
    
    left = ""
    right = ""
    
    
    if l % 2 == 1:
        for i in string[: half ]:
            left += i
        left = left[::-1]

        for i in string[ half+1:  ]:
            right += i
    else:
        for i in string[: half ]:
            left += i
        left = left[::-1]

        for i in string[ half:  ]:
            right += i

    left = int(left)
    right = int(right)
    
#    print(left, right)
    
    if l % 2 == 1:
        if left > right:
#            print("Case 1")
            right = left
            left = str(left)[::-1]
            left = int( left + string[half] )
        elif left <= right:
#            print("Case 2")
            left = str(left)[::-1]
            left = int( left + string[half] )
            left += 1
            left = str(left)
            right = left[:half][::-1]
            
        next_palin = str(left) + str(right)
        
    else:
        if left > right:
#            print("Case 3")
            right = left
        elif left <= right:
#            print("Case 4")
            left = str(left)[::-1]
            left = int(left)
            left += 1
            left = str(left)
            right = left[::-1]
            
        next_palin = str(left) + str(right)
        
    return next_palin

n = int( input() )

for i in range(n):
    string = input()
    
    palin = next_palindrome( list(string) )
    
    print( palin )
