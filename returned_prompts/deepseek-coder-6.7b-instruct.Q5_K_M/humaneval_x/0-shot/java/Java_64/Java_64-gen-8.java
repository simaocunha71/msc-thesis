        int count = 0;
        String lowerCase = s.toLowerCase();

        for (int i = 0; i < s.length(); i++) {
            char c = lowerCase.charAt(i);
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                count++;
            }
        }

        if (lowerCase.endsWith("y")) {
            count++;
        }

        return count;
    }
}




public class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Solution solution = new Solution();
        System.out.println(solution.vowelsCount("abcde"));  // Outputs: 2
        System.out.println(solution.vowelsCount("ACEDY"));  // Outputs: 3
    }
}



Explanation:
The function vowelsCount first converts the string to lowercase. It then iterates over each character in the string. If the character is a vowel, it increments the count. After the loop, if the string ends with 'y' (ignoring case), it increments the count again. Finally, it returns the count.

The time complexity of this function is O(n), where n is the length of the string. This is because it makes a single pass over the string. The space complexity is O(1), as it uses a constant amount of extra space.




























































































































































