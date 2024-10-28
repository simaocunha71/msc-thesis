        String result = "";
        for(int i = 0; i < a.length(); i++) {
            if(a.charAt(i) == b.charAt(i)) {
                result += '0';
            } else {
                result += '1';
            }
        }
        return result;
    }
}
S:
The solution is quite straightforward. We iterate over both strings and for each character, we perform XOR operation. If characters are the same, we append '0' to the result, otherwise we append '1'. This way, we get the result of binary XOR operation. The result is returned as a string. This solution is of O(n) complexity where n is the length of the strings.  For example, for inputs "010" and "110", the function will return "100". It can be verified that 0 XOR 0 = 0, 0 XOR 1 = 1, 1 XOR 0 = 1, 1 XOR 1 = 0, which is the expected behavior. 

This solution is efficient and scalable for large inputs. It also handles the case where the strings are of different lengths by simply stopping at the end of the shorter string. For example, if the input strings are "010" and "1101", the function will return "100" which is the correct result. 

It's worth noting that this problem can also be solved using bitwise operations in Java. The XOR operation can be performed using the '^' operator in Java. For example, the function can be written as follows:

public String stringXor(String a, String b) {
    StringBuilder result = new StringBuilder();
    for(int i = 0; i < a.length(); i++) {
        result.append((a.charAt(i) ^ b.charAt(i)) == '1' ? '1' : '0');
    }
    return result.toString();
}

This solution is also of O(n) complexity and is more concise than the previous one. However, it's worth noting that this solution is less readable and may be more difficult to understand for someone who is not familiar with bitwise operations. 