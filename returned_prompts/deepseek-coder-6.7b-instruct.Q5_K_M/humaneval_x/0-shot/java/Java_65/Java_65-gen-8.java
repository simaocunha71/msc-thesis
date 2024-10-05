        String str = Integer.toString(x);
        int len = str.length();
        if (shift > len) {
            return new StringBuilder(str).reverse().toString();
        }
        String left = str.substring(0, len - shift);
        String right = str.substring(len - shift, len);
        return right + left;
    }
}

This Java program works by converting the integer to a string and then doing a circular shift based on the number of digits. If the shift is larger than the number of digits, the entire number is reversed.

The implementation works by splitting the string into two parts at the index that is the length of the string minus the shift. The part to the right of the split is appended to the start of the string and the part to the left is appended to the end.

The time complexity of this solution is O(n), where n is the number of digits in the number. The space complexity is also O(n) because of the string conversion.
*/

// 