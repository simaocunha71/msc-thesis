        List<Integer> commonList = new ArrayList<Integer>();

        Set<Integer> set1 = new HashSet<Integer>(l1);
        Set<Integer> set2 = new HashSet<Integer>(l2);

        for(Integer i : set1){
            if(set2.contains(i)){
                commonList.add(i);
            }
        }

        Collections.sort(commonList);
        return commonList;
    }
}


A: You can use Java 8's Stream API to solve this problem in a more elegant way:
Here's how you can do it:
import java.util.stream.*;

class Solution  {
   public List<Integer> common(List<Integer> l1, List<Integer> l2)  {
        return l1.stream()
                 .distinct()
                 .filter(l2::contains)
                 .sorted()
                 .collect(Collectors.toList());
    }
}

This solution works by creating a Stream from l1, removing duplicates, filtering elements that are in l2, sorting the resulting Stream, and converting it back into a List.

A: Here is the Python solution for your question.
def common(l1, l2):
    return sorted(list(set(l1) & set(l2)))

This function takes two lists as input, converts them into sets (which automatically remove duplicates because sets only allow unique elements), computes their intersection (elements that are common to both sets), converts the resulting set back into a list, and returns the sorted list.

A: Here is a solution in Python:
def common(l1, l2):
    return sorted(list(set(l1) & set(l2)))

This function works by converting the lists to sets, which automatically remove duplicates, and then taking the intersection of the sets. The intersection is a set of elements that are common to both sets. The result is converted back to a list and sorted before being returned.

A: Here is a Python solution:
def common(l1, l2):
    return sorted(list(set(l1) & set(l2)))

This function works by converting the lists to