import java.util.*;
import java.lang.*;

class Solution {
    /**
    Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> howManyTimes("", "a")
    0
    >>> howManyTimes("aaa", "a")
    3
    >>> howManyTimes("aaaa", "aa")
    3
     */
    public int howManyTimes(String string, String substring) {
        int count = 0;
        for(int i = string.indexOf(substring); i != -1; i = string.indexOf(substring, i + 1)) {
            count++;
        }
        return count;
    }

    /**
    Find all indices where a given substring can be found in the original string.
    >>> findAllIndices("", "a")
    []
    >>> findAllIndices("aaa", "a")
    [0, 1, 2]
    >>> findAllIndices("aaaa", "aa")
    [0, 1, 2, 3]
     */
    public int[] findAllIndices(String string, String substring) {
        List<Integer> indices = new ArrayList<Integer>();
        for(int i = string.indexOf(substring); i != -1; i = string.indexOf(substring, i + 1)) {
            indices.add(i);
        }
        int[] result = new int[indices.size()];
        for(int i = 0; i < result.length; i++) {
            result[i] = indices.get(i);
        }
        return result;
    }
}
