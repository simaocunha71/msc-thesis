        String[] sentences = S.split("[.?!]");
        int count = 0;

        for (String sentence : sentences) {
            if (sentence.trim().length() > 0 && sentence.trim().charAt(0) == 'I') {
                count++;
            }
        }

        return count;
    }
}

The above code will split the string S into sentences using the split() method by the delimiters '.', '?' or '!' and then iterate over each sentence. If the sentence is not empty and starts with the word "I", it counts the boredom.
The final count is returned at the end.




*/

// Main function to test the code
public static void main(String[] args) {
    Solution solution = new Solution();
    System.out.println(solution.isBored("Hello world")); // Should print 0
    System.out.println(solution.isBored("The sky is blue. The sun is shining. I love this weather")); // Should print 1
}

}

/*
Input: String S
Output: integer

Algorithm:
1. Split the input string S into sentences using the split() method by the delimiters '.', '?' or '!'
2. Initialize a counter variable count to 0
3. Iterate over each sentence
    a. If the sentence is not empty and starts with the word "I", increment count by 1
4. Return count

*/

/*
Complexity Analysis:
Time Complexity: O(n), where n is the length of the string S. We are splitting the string into sentences which takes O(n) time. We are also iterating over each sentence to check if it starts with "I", which takes O(n) time. So, the total time complexity is O(n).

Space Complexity: O(n), where n is the length of the string S. We are splitting the string into sentences which results in an array of strings. The space complexity is O(n).
*/

// End of the code


































