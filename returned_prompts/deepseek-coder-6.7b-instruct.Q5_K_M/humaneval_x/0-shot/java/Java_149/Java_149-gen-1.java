        List<String> newList = new ArrayList<>();
        for (String s : lst) {
            if (s.length() % 2 == 0) {
                newList.add(s);
            }
        }

        Collections.sort(newList, new Comparator<String>(){
            public int compare(String s1, String s2){
                if (s1.length() != s2.length())
                    return s1.length() - s2.length();
                else
                    return s1.compareTo(s2);
            }});

        return newList;
    }
}

Explanation:
- The function `listSort` takes in a list of strings `lst`.
- We first create a new list `newList` to store the strings with even lengths.
- We then loop through each string `s` in `lst`, and if the length of `s` is an even number, we add it to `newList`.
- After that, we sort `newList` using a custom comparator. This comparator first checks if the lengths of two strings are different. If they are, it returns the difference in lengths. If they are the same, it returns the result of comparing the two strings lexicographically (alphabetically).
- Finally, we return the sorted list `newList`.
- This function will return the list of strings with even lengths sorted by length and alphabetically.
- It assumes that all words will have the same length.
*/

/*
Test cases:
assert listSort(Arrays.asList("aa", "a", "aaa")) => ["aa"]
assert listSort(Arrays.asList("ab", "a", "aaa", "cd")) => ["ab", "cd"]
assert listSort(Arrays.asList("abc", "def", "ghi", "jk")) => ["ghi", "jk"]
assert listSort(Arrays.asList("abc", "de", "ghi", "j")) => ["de", "j"]
assert listSort(Arrays.asList("abcde", "abc", "a", "abcd")) => ["abcde", "abcd"]
*/

/*
Time Complexity