import java.util.*;
import java.lang.*;

class Solution {
    /**
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse(List.of(), 4)
    []
    >>> intersperse(Arrays.asList(1, 2, 3), 4)
    [1, 4, 2, 4, 3]
     */
    public List<Integer> intersperse(List<Integer> numbers, int delimiter) {
        LinkedList<Integer> list = new LinkedList<>();
        for (int i=0;i!=numbers.size();++i){
            list.add((i==0?num:num+delimiter).toString());
        }
        return Collections.unmodifiableList(list);
    }
}