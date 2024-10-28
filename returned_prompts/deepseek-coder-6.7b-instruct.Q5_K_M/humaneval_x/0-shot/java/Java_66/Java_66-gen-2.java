        int sum = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isUpperCase(c)) {
                sum += (int) c;
            }
        }
        return sum;
    }
}

This code works by iterating over each character in the string. If the character is uppercase, it adds its ASCII value to the sum. The result is the sum of the ASCII values of all uppercase characters in the string.
*/

class Main {
    public static void main (String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.digitSum("abAB")); // 131
        System.out.println(sol.digitSum("abcCd")); // 67
        System.out.println(sol.digitSum("helloE")); // 69
        System.out.println(sol.digitSum("woArBld")); // 131
        System.out.println(sol.digitSum("aAaaaXa")); // 153
    }
}

// Explanation:
// The ASCII value for 'A' is 65, for 'B' is 66, and so on.
// So, the sum of the uppercase letters in the string "abAB" is 65 (from 'A' in the first 'AB') + 65 (from 'A' in the second 'AB') = 130.
// The sum of the uppercase letters in the string "abcCd" is 65 (from 'A') + 67 (from 'C') = 132.
// The sum of the uppercase letters in the string "helloE" is 69 (from 'E').
// The sum of the uppercase letters in the string "woArBld" is 65 (from 'A') + 66 (from 'B') + 68 (from 'd').
// The sum of the uppercase letters in the string "aAaaaXa" is 88 (from 'X').
// So, the function digitSum should return 13