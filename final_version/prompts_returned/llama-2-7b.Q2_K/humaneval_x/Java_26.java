import java.util.*;
import java.lang.*;
import java.util.stream.Collectors;

class Solution {
    /**
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> removeDuplicates(Array.asList(1, 2, 3, 2, 4))
    [1, 3, 4]
     */
    public List<Integer> removeDuplicates(List<Integer> numbers) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int num:numbers ) {
            if (!map.containsKey(num)) {
                map.put(num , 1);
            }else{
                map.put(num , map.get(num) + 1);
            }
        }
        List<Integer> ret = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry:map.entrySet()) {
            if (entry.getValue()==1){
                ret.add(entry.getKey());
            }else{
                if (entry.getValue()!=0)
                    ret.add(entry.getKey());
             }
        }
        return ret;
    }
}
