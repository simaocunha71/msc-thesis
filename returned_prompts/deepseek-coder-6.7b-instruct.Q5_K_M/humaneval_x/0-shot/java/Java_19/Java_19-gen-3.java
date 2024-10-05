        String[] words = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        String[] nums = numbers.split(" ");
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < words.length; i++) {
            map.put(words[i], i);
        }
        Arrays.sort(nums, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return map.get(o1) - map.get(o2);
            }
        });
        return String.join(" ", nums);
    }
}

The solution creates a HashMap to map words to their respective numbers. Then it sorts the array of words using a custom Comparator that compares the mapped numbers. Finally, it joins the array of words back into a string with spaces in between.
The time complexity of this solution is O(n log n), where n is the number of words in the input string. This is because the sorting step dominates the complexity. The space complexity is O(n), which is the space required to store the words in the input string.
*/

