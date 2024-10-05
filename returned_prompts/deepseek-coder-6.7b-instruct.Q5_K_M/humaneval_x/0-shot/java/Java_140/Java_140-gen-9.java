        StringBuilder result = new StringBuilder();
        boolean isPrevSpace = false;
        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            if (c == ' ') {
                if (isPrevSpace) {
                    result.append('-');
                } else {
                    result.append('_');
                }
                isPrevSpace = true;
            } else {
                result.append(c);
                isPrevSpace = false;
            }
        }
        return result.toString();
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.fixSpaces("Example")); // Example
        System.out.println(solution.fixSpaces("Example 1")); // Example_1
        System.out.println(solution.fixSpaces(" Example 2")); // _Example_2
        System.out.println(solution.fixSpaces(" Example  3")); // _Example-3
    }
}

This solution works by iterating through each character of the text. If it's a space, it checks if the previous character was also a space. If yes, it adds a - to the result. If no, it adds a _ to the result. If the character is not a space, it adds the character to the result and sets isPrevSpace to false.

Time complexity: O(n)
Space complexity: O(n)
*/

// Please, do not use System.out.println in your solution. It is used here for debugging only.

// The code you submit should be your class named Solution.
// It should contain the method fixSpaces(String text).
// The signature of the method should be public.

// You can add any extra imports you need, but you may not use any other classes than the ones imported.
// You may not use any other methods than those available in the String and StringBuilder classes.
// You may not use any other classes than those imported.

// You may not use any other data structures than those available in the java.util package.
// You may not use any