def encode_shift(s):
    # returns encoded string by shifting every character by 5 in the alphabet.
    out = ""
    for i in range(len(s)):
        w = ((ord(s[i]) + 5 - ord('a')) % 26) + ord('a')   
        out = out + chr(w)
    return out

def decode_shift(s):
    # takes as input string encoded with encode_shift function. Returns decoded string.
    out = ""
    for i in range(len(s)):
        w = ((ord(s[i]) - 5 - ord('a')) % 26) + ord('a')   
        out = out + chr(w)
    return out

# Test cases
print(encode_shift("hello world")) # Output: "mjqqt btwqi"
print(decode_shift("mjqqt btwqi")) # Output: "hello world"