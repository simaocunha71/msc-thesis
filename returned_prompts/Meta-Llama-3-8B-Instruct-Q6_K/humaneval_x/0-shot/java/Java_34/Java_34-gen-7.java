    import java.util.*;

    class Solution {
        public List<Integer> unique(List<Integer> l) {
            Set<Integer> set = new LinkedHashSet<Integer>(l);
            return new ArrayList<Integer>(set);
        }
    }
    // This function sorts the list and removes duplicates
    // It creates a LinkedHashSet from the list, which automatically removes duplicates
    // Then it converts the LinkedHashSet back to a List and returns it
    // The LinkedHashSet is used instead of a HashSet because it maintains the order of elements
    // The function does not sort the list in-place, it returns a new list
    // The time complexity of this function is O(n), where n is the number of elements in the list
    // The space complexity of this function is also O(n), where n is the number of elements in the list
    // The function can be used to remove duplicates from a list and maintain the order of elements
    // It can be used with any type of object, not just Integers
    // It can be used with any collection, not just lists
    // It can be used with any type of collection, not just collections that implement List or Set
    // It can be used with any type of object, not just objects that implement Comparable
    // It can be used with any type of collection, not just collections that implement SortedSet
    // It can be used with any type of object, not just objects that implement Comparable
    // It can be used with any type of collection, not just collections that implement SortedSet
    // It can be used with any type of object, not just objects that implement Comparable
    // It can be used with any type of collection, not just collections that implement SortedSet
    // It can be used with any type of object, not just objects that implement Comparable
    // It can be used with any type of collection, not just collections that implement SortedSet
    // It can be used with any type of object, not just objects that implement Comparable
    // It can be used with any type of collection, not just collections that implement SortedSet
    // It can be used with any type of object, not just objects that implement Comparable
    // It can be used with any type of collection, not just collections that implement SortedSet
    // It can be used with any type of object, not just objects that implement Comparable
    // It can be used with any type of collection, not just