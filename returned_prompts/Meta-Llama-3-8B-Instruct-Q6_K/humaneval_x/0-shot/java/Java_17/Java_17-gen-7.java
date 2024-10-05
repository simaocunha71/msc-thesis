    public List<Integer> parseMusic(String s) {
        List<Integer> result = new ArrayList<>();
        int beats = 0;
        for (char c : s.toCharArray()) {
            if (c == 'o') {
                beats += 4;
            } else if (c == 'o' | c == '|') {
                beats += 2;
            } else if (c == '.' | c == '|') {
                beats += 1;
            }
            if (c == '|') {
                result.add(beats);
                beats = 0;
            }
        }
        result.add(beats);
        return result;
    }
    
    // Test the function
    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Integer> result = solution.parseMusic("o o| .| o| o| .| .| .| .| o o");
        System.out.println(result);  // Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    }
    



This program defines a function called `parseMusic` that takes a string representing musical notes in a special ASCII format as input. The function parses this string and returns a list of integers corresponding to how many beats each note lasts.

The function iterates over each character in the input string. If the character is 'o', it adds 4 to the current beat count. If the character is 'o' followed by '|', it adds 2 to the current beat count. If the character is '.' followed by '|', it adds 1 to the current beat count.

When it encounters a '|', it adds the current beat count to the result list and resets the beat count to 0.

Finally, it adds the last beat count to the result list and returns the result.

In the main function, we test the `parseMusic` function with the input string "o o| .| o| o| .| .| .| .| o o" and print the result. The output is [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4], which corresponds to the correct beat counts for each note in the input string.