import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.

    Example:
    histogram("a b c") == {"a": 1, "b": 1, "c": 1}
    histogram("a b b a") == {"a": 2, "b": 2}
    histogram("a b c a b") == {"a": 2, "b": 2}
    histogram("b b b b a") == {"b": 4}
    histogram("") == {}
     */
    public Map<String, Integer> histogram(String test) {
        HashMap<String, Integer> map = new HashMap<>();
        
        char[] alphabets = test.toCharArray();
        List<Character> list = Arrays.asList(alphabets); 

        for (Character ch : list){
            if(map.containsKey(ch.toString())){
                map.put(ch.toString(), (int)((Double)map.get(ch.toString())+1));
            }
            else{
                map.put(ch.toString(), 1);
            }
        }
        
        for(Entry<String, Integer> entry : map.entrySet()){
            if(entry.getValue()>=1){
                System.out.println("key: " + entry.getKey());
                System.out.println("value:" + entry.getValue());
            }
        }
        
        return map;
    }
    
}