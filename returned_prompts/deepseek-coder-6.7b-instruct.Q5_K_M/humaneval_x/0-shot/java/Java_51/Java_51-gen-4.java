        StringBuilder builder = new StringBuilder();
        String vowels = "aeiouAEIOU";
        for (char c : text.toCharArray()) {
            if (vowels.indexOf(c) == -1) {
                builder.append(c);
            }
        }
        return builder.toString();
    }
}

This solution works by iterating through each character in the input string, checking if it is a vowel using the indexOf method from the String class, and if it is not a vowel, appending it to the StringBuilder instance. The StringBuilder instance is then converted back to a string and returned.

This solution has a time complexity of O(n), where n is the length of the input string, since it needs to iterate through the string once. The space complexity is also O(n), as the StringBuilder instance is used to store the result.

The indexOf method used in this solution is a O(1) operation for the English alphabet, so it is efficient for checking if a character is a vowel.
*/

