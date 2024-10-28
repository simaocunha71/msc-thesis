        List<Integer> commonList = new ArrayList<Integer>();
        for(Integer i : l1) {
            if(l2.contains(i)) {
                commonList.add(i);
                l2.remove(i);
            }
        }

        Collections.sort(commonList);
        return commonList;
    }
}


A: Your code is almost correct, but it fails to handle cases where an element is present in both lists. Specifically, when an element is found in l1, it's removed from l2, but this might also remove an element that is present in l1 later.
You could use a Set instead of a List for l2, as Sets do not allow duplicate elements.
Also, you could use Java 8's Streams to make the code a bit cleaner and more readable.
Here is the corrected code:
import java.util.*;
import java.util.stream.*;

class Solution {
    public List<Integer> common(List<Integer> l1, List<Integer> l2) {
        Set<Integer> set = new HashSet<>(l2);
        List<Integer> commonList = l1.stream()
 .filter(set::contains)
 .distinct()
 .sorted()
 .collect(Collectors.toList());
        return commonList;
    }
}

This code creates a Set from l2, then uses the stream API to filter l1 for elements that are present in the set. The distinct() function ensures that each element is only added once to the result, and the sorted() function sorts the result. Finally, collect() is used to convert the stream back to a List.

A: You can use Java 8's Streams and Collectors to simplify your code:
import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public List<Integer> common(List<Integer> l1, List<Integer> l2) {
        return l1.stream()
                 .filter(l2::contains)
                 .distinct()
                 .sorted()
                 .collect(Collectors.toList());
    }
}

This code creates a Stream from l1, then filters it