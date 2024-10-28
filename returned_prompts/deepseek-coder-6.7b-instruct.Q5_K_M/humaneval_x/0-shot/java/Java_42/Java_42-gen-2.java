        return l.stream().map(i -> i + 1).collect(Collectors.toList());
    }
}

This solution uses Java 8 Stream API to map each element of the list to itself incremented by 1.

A: The correct answer is:
import java.util.*;
import java.lang.*;
import java.util.stream.Collectors;

class Solution {
    /**
    Return list with elements incremented by 1.
    >>> incrList(Arrays.asList(1, 2, 3))
    [2, 3, 4]
    >>> incrList(Arrays.asList(5, 3, 5, 2, 3, 3, 9, 0, 123))
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    */
    public List<Integer> incrList(List<Integer> l) {
        return l.stream().map(i -> i + 1).collect(Collectors.toList());
    }
}

This solution uses Java 8 Stream API to map each element of the list to itself incremented by 1.

A: Here is the correct solution:
import java.util.*;
import java.lang.*;
import java.util.stream.Collectors;

class Solution {
    /**
    Return list with elements incremented by 1.
    >>> incrList(Arrays.asList(1, 2, 3))
    [2, 3, 4]
    >>> incrList(Arrays.asList(5, 3, 5, 2, 3, 3, 9, 0, 123))
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    */
    public List<Integer> incrList(List<Integer> l) {
        return l.stream().map(i -> i + 1).collect(Collectors.toList());
    }
}

This solution uses Java 8 Stream API to map each element of the list