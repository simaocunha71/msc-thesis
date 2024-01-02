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
        Map<Character, Integer> map = new HashMap<>();
        for (String w : words){
            char[] chars = w.toCharArray();
            for(int i=0;i<chars.length ;i++){
                if(!map.containsKey(chars[i]) && !map.containsValue(1)){
                    map.put(chars[i], 1);
                }else{
                    int count = map.getAndUpdate((Character) (int) chars[i], old -> {
                        return old + 1;
                    });
                    if (count > map.get(chars[i])){
                        map.put(chars[i], -1);
                    }
                }
            }
        }
        for(Map.Entry<Character, Integer> e : map.entrySet()){
            System.out.print("{},");
        }
        return "";
        
    }
    
}