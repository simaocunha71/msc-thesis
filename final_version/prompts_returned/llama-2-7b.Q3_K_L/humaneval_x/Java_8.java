import java.util.*;
import java.lang.*;

class Solution {
    /**
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sumProduct(List.of())
    [0, 1]
    >>> sumProduct(Arrays.asList(1, 2, 3, 4))
    [10, 24]
     */
    public List<Integer> sumProduct(List<Integer> numbers) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i : numbers){
            if(map.containsKey(i)){
                map.put(i, map.get(i)+1); 
            }else{
                 map.put(i, 1);
             }
         }
          return Arrays.asList(map.entrySet().stream()
              .sorted((e1, e2) -> e1.getValue().compareTo(e2.getValue())).collect(Collectors.toList()))
                   .get(0).getValue();
    }
}