        String[] words = s.split(" ");
        String result = "";
        for(String word: words){
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            result += new String(chars) + " ";
        }
        return result.trim();
    }
```

In the solution, we firstly split the string into words. Then, we sort each word's characters and append the sorted word to the result string. Finally, we return the result string.

This solution has a time complexity of O(nlogn) because of the sorting operation, where n is the length of the string. The space complexity is O(n) because we store the sorted characters in a new string.

This solution assumes that words are separated by a single space and that the order of words in the sentence is to be preserved.

Note: This solution works for ASCII characters only. For Unicode characters, you would need to use a different sorting algorithm that handles Unicode characters correctly.
