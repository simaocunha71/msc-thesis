        List<Integer> result = new ArrayList<Integer>();
        Set<Integer> set1 = new HashSet<Integer>(l1);
        Set<Integer> set2 = new HashSet<Integer>(l2);

        for(Integer s : set1){
            if(set2.contains(s)){
                result.add(s);
            }
        }

        Collections.sort(result);
        return result;
    }
}


A: The problem with your current code is that you are not removing elements from set2 once they have been found in set1. This means that you are still checking for common elements in set2, even if you've already found them in set1.
Here is the corrected code:
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> common(List<Integer> l1, List<Integer> l2) {
        List<Integer> result = new ArrayList<Integer>();
        Set<Integer> set1 = new HashSet<Integer>(l1);
        Set<Integer> set2 = new HashSet<Integer>(l2);

        for (Integer s : set1) {
            if (set2.contains(s)) {
                result.add(s);
                set2.remove(s); // remove common element from set2
            }
        }

        Collections.sort(result);
        return result;
    }
}

This code will remove elements from set2 once they have been found in set1, so you won't be checking for common elements in set2 that you've already found in set1.

A: Here's a way to do it using Java 8's streams:
import java.util.*;
import java.util.stream.*;

class Solution {
    public List<Integer> common(List<Integer> l1, List<Integer> l2) {
        return l1.stream()
                 .distinct()
                 .filter(i -> l2.contains(i))
                 .sorted()
                 .collect(Collectors.toList());
    }
}

This code works by creating a stream from l1, removing duplicates,