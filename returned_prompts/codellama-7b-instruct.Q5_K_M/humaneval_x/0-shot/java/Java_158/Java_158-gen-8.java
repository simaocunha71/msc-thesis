import java.util.*;
import java.lang.*;

class Solution {
    /**
    Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    findMax(["name", "of", "string"]) == "string"
    findMax(["name", "enam", "game"]) == "enam"
    findMax(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
     */
    public String findMax(List<String> words) {
        if(words == null || words.size() == 0) return "";
        int max = 0;
        int count = 0;
        String word = "";
        for(int i = 0; i < words.size(); i++)
        {
            Set<Character> set = new HashSet<>();
            for(char c : words.get(i).toCharArray())
            {
                set.add(c);
            }
            if(set.size() > max)
            {
                max = set.size();
                count = 1;
                word = words.get(i);
            }
            else if(set.size() == max)
            {
                if(words.get(i).compareTo(word) < 0)
                {
                    count = 1;
                    word = words.get(i);
                }
            }
        }
        if(count == 1) return word;
        else return "";
    }
}

B:
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    findMax(["name", "of", "string"]) == "string"
    findMax(["name", "enam", "game"]) == "enam"
    findMax(["