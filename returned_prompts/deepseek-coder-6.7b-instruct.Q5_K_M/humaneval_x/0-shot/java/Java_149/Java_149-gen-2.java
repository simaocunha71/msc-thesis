        List<String> result = new ArrayList<>();
        for (String s : lst) {
            if (s.length() % 2 == 0) {
                result.add(s);
            }
        }
        Collections.sort(result, new Comparator<String>() {
            public int compare(String s1, String s2) {
                if (s1.length() != s2.length()) {
                    return s1.length() - s2.length();
                } else {
                    return s1.compareTo(s2);
                }
            }
        });
        return result;
    }
}

This function works by first creating a new list and adding only the strings that have even lengths to it. Then it sorts this new list. The sorting is done using a custom comparator that first compares the lengths of the strings, and if they are the same, it compares the strings alphabetically.

Testing:
assert listSort(Arrays.asList("aa", "a", "aaa")) == ["aa"]
assert listSort(Arrays.asList("ab", "a", "aaa", "cd")) == ["ab", "cd"]
assert listSort(Arrays.asList("ab", "a", "aaa", "cd", "efg", "b")) == ["ab", "b", "cd", "efg"]
assert listSort(Arrays.asList("ab", "a", "aaa", "cd", "efg", "b", "hij")) == ["ab", "b", "cd", "efg", "hij"]
assert listSort(Arrays.asList("ab", "a", "aaa", "cd", "efgh", "b")) == ["ab", "b"]
assert listSort(Arrays.asList("ab", "a", "aaa", "cd", "efgh", "b", "hijk")) == ["ab", "b"]
assert listSort(Arrays.asList("ab", "a", "aaa", "cd", "efgh", "b", "hijk", "l")) == ["ab", "b", "l"]

This solution will work for any list of strings, as