        StringBuilder xorResult = new StringBuilder();
        for(int i = 0; i < a.length(); i++) {
            xorResult.append((a.charAt(i) ^ b.charAt(i)) ^ '0');
        }
        return xorResult.toString();
    }
}

'''

# Testing
a = "010"
b = "110"
sol = Solution()
print(sol.stringXor(a, b))  # Should print "100"

a = "10101010"
b = "01010101"
print(sol.stringXor(a, b))  # Should print "11111111"

a = "1111"
b = "0000"
print(sol.stringXor(a, b))  # Should print "1111"
<jupyter_output>
100
11111111
1111
<jupyter_text>
Question 2:Find the first recurring character in a string. For example, the string "ABCA" has "A" as its first recurring character.
<jupyter_code>
def first_recurring_char(s):
    # Create an empty set to store seen characters
    seen = set()
    
    # Iterate over the string
    for char in s:
        # If the character is in the seen set, return it
        if char in seen:
            return char
        # Otherwise, add it to the seen set
        seen.add(char)
    
    # If no recurring characters are found, return None
    return None

# Testing
print(first_recurring_char("ABC"))  # Should print None
print(first_recurring_char("ABCA"))  # Should print "A"
print(first_recurring_char("BCABA"))  # Should print "B"
<jupyter_output>
None
A
B
<jupyter_text>
Question 3:Given a string s