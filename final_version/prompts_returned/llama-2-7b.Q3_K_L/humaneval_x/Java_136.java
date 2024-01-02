import java.util.*;
import java.lang.*;

class Solution {
    /**
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largestSmallestIntegers(Arrays.asList(2, 4, 1, 3, 5, 7)) == (Optional.empty(), Optional.of(1))
    largestSmallestIntegers(Arrays.asList()) == (Optional.empty(), Optional.empty())
    largestSmallestIntegers(Arrays.asList(0)) == (Optional.empty(), Optional.empty())
     */
    public List<Optional<Integer>> largestSmallestIntegers(List<Integer> lst){
        ArrayList<Integer> a = new ArrayList<>();
        ArrayList<Integer> b = new ArrayList<>();

        Iterator itr = lst.iterator();
        if (itr.hasNext())
            a.add(itr.next());
        
        while (itr.hasNext()){
            b.add(itr.next());
        }
        
        int max = Math.max(a.stream().mapToInt((i)-> {return i;}).toArray())[0];
        int min = Math.min(b.stream().mapToInt((i)-> {return i;}).toArray())[0];
        
        if (max == -1 || b.size() == 0) return new ArrayList<>(2);
        else if (min == -1 || a.size() == 0) return new ArrayList<>(2);
        else{
            return new ArrayList<>(Arrays.asList(new Optional<>(max), new Optional<>(min)));
        }
    }
}