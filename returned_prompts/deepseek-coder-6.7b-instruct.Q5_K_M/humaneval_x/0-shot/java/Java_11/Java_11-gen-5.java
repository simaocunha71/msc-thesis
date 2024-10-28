        String result = "";
        
        for(int i = 0; i < a.length(); i++) {
            if(a.charAt(i) == b.charAt(i)) {
                result += "0";
            } else {
                result += "1";
            }
        }
        
        return result;
    }
}

Explanation:
The logic is to iterate over each character of the two strings at the same index. If the characters are the same, append '0' to the result string, else append '1'. This gives us the XOR of two binary numbers.

Time Complexity: O(n) where n is the length of the input strings.
Space Complexity: O(n) to store the result string.

In Python:

def stringXor(a, b):
    result = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"
    return result
'''
>>> stringXor("010", "110")
'100'
'''
'''
Python also has a built-in operator '^' for bitwise XOR operation.
'''
'''
def stringXor(a, b):
    return bin(int(a, 2) ^ int(b, 2))[2:]
'''
>>> stringXor("010", "110")
'100'
'''
'''
The bin function converts the integer result to binary and [2:] is used to remove the '0b' prefix.
'''
'''
def stringXor(a, b):
    return format(int(a, 2) ^ int(b, 2), 'b')
'''
>>> stringXor("010", "110")
'100'
'''
'''
The format function is used to convert the integer result to binary and 'b' is used to remove the '0b' prefix.
'''
'''
def stringXor(a, b):
    return ''.join('1' if x