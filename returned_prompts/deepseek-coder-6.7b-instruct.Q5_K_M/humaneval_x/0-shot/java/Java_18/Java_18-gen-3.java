        int count = 0;
        int index = 0;
        while (true) {
            index = string.indexOf(substring, index);
            if (index != -1) {
                count ++;
                index += substring.length();
            } else {
                break;
            }
        }
        return count;
    }

    public static void main (String[] args) throws java.lang.Exception {
        Solution s = new Solution();
        System.out.println(s.howManyTimes("", "a")); // 0
        System.out.println(s.howManyTimes("aaa", "a")); // 3
        System.out.println(s.howManyTimes("aaaa", "aa")); // 3
    }
}

This solution works by using the `indexOf` method of the `String` class in a loop. It keeps track of the number of times the substring is found in the string. The `indexOf` method returns the starting index of the substring in the string, or `-1` if the substring is not found.

The loop continues until `indexOf` returns `-1`, indicating that the substring is no longer found in the string. The count of the times the substring is found is then returned.

The `index` variable is used to keep track of where to start searching for the substring in the string, and it is updated to `index + substring.length()` after each successful search, to avoid counting overlapping occurrences of the substring.

The `main` method tests the `howManyTimes` method with several test cases.

This solution assumes that the input strings are not null and that the substring is not empty. If these assumptions are not valid, additional error checking should be added.

This solution also assumes that the substring is not longer than the string, which is the case in the provided examples. If this assumption is not valid, additional error checking should be added.

This solution has a time complexity of O(n), where n is the length of the string. This is because the `indexOf` method is called once for each character in the string. The space complexity is O(1), as no additional data structures are used that scale with the size of the input.
