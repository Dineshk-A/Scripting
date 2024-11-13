def palindrome(x: int)-> bool:
    number = x 
    reverse = 0

    while number :
        reverse = reverse * 10 + number % 10 
        number //= 10 
    return x == reverse 

x = 121 
result =  palindrome(x)
print(result)

#Time Complexity
#Since we are going through the entire number digit by digit, the time complexity should be O(log10n).
#The reason behind log10 is because we are dealing with integers which are base 10.

#Space Complexity
#We are not using any data structure for interim operations, therefore, the space complexity is O(1).

