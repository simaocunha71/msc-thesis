        Set<Character> set = new HashSet<>();
        for (int i = 0; i < string.length(); i++) {
            set.add(Character.toLowerCase(string.charAt(i)));
        }
        return set.size();
    }
}

Solution:
The solution uses a set to store distinct characters. Each character is converted to lowercase before it is added to the set. This ensures that the same characters in different cases are considered the same. The size of the set is then returned, which gives the number of distinct characters in the string.
*/

