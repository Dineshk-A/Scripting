def roman_integer(s: str) -> int:
    res = 0
    roman = {"I" : 1 , "V" : 5 ,  "X" : 10 , "L" : 50 , "C" : 100 , "D": 500 , "M" : 1000}

    for i in range(len(s)):
        if i + 1 < (len(s)) and roman[s[i]] < roman[s[i + 1]]:
            res -= roman[s[i]]
        else:
            res += roman[s[i]]
    return res

s = "LVIII"
result = roman_integer(s)
print(result)

#time complexity is gonna be O(n) scan through the entire input string .
#space complexity is gonna be O(1) as we dont use data structures and no additonal memory used as we are gonna use hash map which we determine and no extra variable than the 7 ones .