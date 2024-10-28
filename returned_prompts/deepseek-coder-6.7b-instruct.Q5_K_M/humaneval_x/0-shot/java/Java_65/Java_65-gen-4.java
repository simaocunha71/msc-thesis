        String str = String.valueOf(x);
        int length = str.length();

        if (shift > length) {
            StringBuilder sb = new StringBuilder(str);
            return sb.reverse().toString();
        }

        String shifted = str.substring(length - shift) + str.substring(0, length - shift);
        return shifted;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.circularShift(12, 1)); // 21
        System.out.println(s.circularShift(12, 2)); // 12
        System.out.println(s.circularShift(1234, 2)); // 3412
        System.out.println(s.circularShift(1234, 5)); // 4321
    }
}

The main() function is a driver function that tests the circularShift() method with various inputs.
The circularShift() method converts the input integer to a string and calculates the length. If the shift is greater than the length, it reverses the string. Otherwise, it performs a circular shift by taking a substring of the end part of the string and concatenating it with the start part of the string.
The reversed and shifted string is returned as the result.
This solution assumes that the input integer is positive. If negative numbers are allowed, the code would need to be adjusted accordingly.



































































































































































