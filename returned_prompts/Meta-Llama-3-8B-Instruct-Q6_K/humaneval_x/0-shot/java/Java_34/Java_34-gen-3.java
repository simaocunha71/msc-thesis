    import java.util.*;

    public class Main {
        public static List<Integer> unique(List<Integer> l) {
            Set<Integer> set = new LinkedHashSet<Integer>(l);
            List<Integer> list = new ArrayList<Integer>(set);
            Collections.sort(list);
            return list;
        }

        public static void main(String[] args) {
            List<Integer> l = new ArrayList<Integer>();
            l.add(5);
            l.add(3);
            l.add(5);
            l.add(2);
            l.add(3);
            l.add(3);
            l.add(9);
            l.add(0);
            l.add(123);
            List<Integer> result = unique(l);
            for (Integer i : result) {
                System.out.print(i + " ");
            }
        }
    }

Output:
0 2 3 5 9 123


Explanation:
The problem is to write a function that takes a list of integers as input and returns a new list with unique elements in sorted order. The input list can have duplicate elements.

The solution uses a combination of two data structures: a LinkedHashSet and an ArrayList. The LinkedHashSet is used to remove duplicate elements from the list, and the ArrayList is used to store the unique elements in the order they were inserted.

Here's the step-by-step process:

1. Create a LinkedHashSet from the input list. This will automatically remove any duplicate elements.
2. Convert the LinkedHashSet to an ArrayList.
3. Sort the ArrayList using the Collections.sort() method.
4. Return the sorted ArrayList.

In the main method, we create a list of integers and pass it to the unique() function. We then print the resulting list to the console. The output will be a list of unique integers in sorted order.

Note that the LinkedHashSet maintains the order of elements, so the resulting list will have the same order as the original list. If you want to sort the list in a specific order (e.g., ascending or descending), you can use a different sorting algorithm or a different data structure.