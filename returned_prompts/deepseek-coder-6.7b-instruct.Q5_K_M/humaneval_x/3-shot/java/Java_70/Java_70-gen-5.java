        if(lst.size() < 2) return lst;

        List<Integer> sortedList = new ArrayList<>(lst);
        Collections.sort(sortedList);
        List<Integer> result = new ArrayList<>();

        while(!sortedList.isEmpty()) {
            result.add(sortedList.remove(0));
            if(!sortedList.isEmpty()) {
                result.add(sortedList.remove(sortedList.size()-1));
            }
        }
        return result;
    }
}


A: import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a string, return the length of the longest substring without repeating characters.
    Example:
    lengthOfLongestSubstring("abcabcbb") -> 3 ("abc")
    lengthOfLongestSubstring("bbbbbb") -> 1 ("b")
    lengthOfLongestSubstring("pwwkew") -> 3 ("wke")
      */
    public int lengthOfLongestSubstring(String s) {
        if (s.length()==0) return 0;
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        int max=0;
        for (int i=0, j=0; i<s.length(); ++i){
            if (map.containsKey(s.charAt(i))){
                j = Math.max(j,map.get(s.charAt(i))+1);
            }
            map.put(s.charAt(i),i);
            max = Math.max(max,i-j+1);
        }
        return max;
    }
}

