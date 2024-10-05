        List<String> sortedList = new ArrayList<String>();

        for (String word : lst) {
            if (word.length() % 2 == 0) {
                sortedList.add(word);
            }
        }

        Collections.sort(sortedList, new Comparator<String>() {
            public int compare(String s1, String s2) {
                if (s1.length() != s2.length()) {
                    return s1.length() - s2.length();
                } else {
                    return s1.compareTo(s2);
                }
            }
        });

        return sortedList;
    }
}

In this code, the function listSort takes a list of strings as input. It initializes an empty list sortedList. It then iterates over the input list, and if a word has an even length, it adds it to the sortedList. Finally, the function sorts the sortedList by length of each word and alphabetically for words of the same length using a custom Comparator, and returns the sorted list.

The function then returns the sortedList. The sortedList is sorted by length of each word and alphabetically for words of the same length using a custom Comparator. The sortedList is returned as the result.

The time complexity of this code is O(n log n), where n is the number of elements in the list. This is because the list is sorted using the Collections.sort method, which has a time complexity of O(n log n).

The space complexity of this code is O(n), where n is the number of elements in the list. This is because the sortedList stores the elements of the input list.

Please note that in the code, the function assumes that all words will have the same length. If this is not the case, the function may not work as expected.

This code is written in Java.

The code does not contain any error handling or edge case handling. It assumes that the input will always be a list of strings.

The code does not contain any comments or documentation. It is intended to be self-explanatory.

Please let me know if you have any questions or need further clarification.
    */
}

import java.util.*;