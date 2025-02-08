#count no of unique characters 
input_string = "aaaabcc"
char_count = {}

for char in input_string:
    if char in char_count:
        char_count[char] = char_count[char] + 1
    else:
        char_count[char] = 1

for char, count in char_count.items():
    print(f"{char} count is {count}")