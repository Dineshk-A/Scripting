def palindrome(x: int) -> bool:
    if x < 0: return False 

    div = 1
    while x >= 10 * div :
        div *= 10
    while x :
        if x // div != x % 10 : return False

        x = (x % div) // 10
        div = div // 100
    return True

x = int(input())
result = palindrome(x)
print(result)

# 121 true , -121 false , 10 false 
# check time space complexity
#o(log(x)) has while loop runs till x becomes lesser than 10 * div and also x // 10 and x % 10 removing the left and right
#hece time is o(log(x)) and space div remains constant regardless of input size hence sc is 0(1)