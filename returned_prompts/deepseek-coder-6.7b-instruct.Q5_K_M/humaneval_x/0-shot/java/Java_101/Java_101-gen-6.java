        // Initialize an arraylist to store the words
        ArrayList<String> words = new ArrayList<String>();
        
        // Use the split function to separate the string into words
        // This function separates the string at each occurrence of the pattern it's given
        // In this case, we're separating at each space or comma
        for(String word: s.split("\\s|,")){
            words.add(word);
        }
        
        return words;
    }
}

This solution works by first initializing an empty ArrayList of Strings. The split function is used to separate the input string at each space or comma. The result is each word in the string stored in the ArrayList. This ArrayList is then returned by the function.
*/

/*
Testcases:

Input: "Hi, my name is John"
Output: ["Hi", "my", "name", "is", "John"]

Input: "One, two, three, four, five, six"
Output: ["One", "two", "three", "four", "five", "six"]

Input: "A quick brown fox, jumps over the lazy dog"
Output: ["A", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]

Input: "A sentence with multiple,  spaces, and commas"
Output: ["A", "sentence", "with", "multiple", "spaces", "and", "commas"]
*/

// This is a sample testcase to check your solution
// You can add more testcases according to your requirements
class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        System.out.println(solution.wordStrings("Hi, my name is John"));
        System.out.println(solution.wordStrings("One, two, three, four, five, six"));
        System.out.println(solution.wordStrings("A quick brown fox, jumps over the lazy dog"));
        System.out.println(solution.wordStrings("A sentence with multiple,  spaces, and commas"));
    }
}

// The output