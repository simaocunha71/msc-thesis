Here is a solution to the problem:
```
public boolean triplesSumToZero(List<Integer> l) {
    Set<Integer> set = new HashSet<>(l);
    for (int num : set) {
        if (set.contains(-num) && set.contains(num * 2)) {
            return true;
        }
    }
    return false;
}
```
Explanation:

The problem asks to find three distinct elements in the list that sum to zero. We can use a set to store the elements of the list to avoid duplicates and to make it easier to check for the presence of an element.

We iterate over the set, and for each element, we check if its negative is also present in the set. If it is, we know that there are two elements that sum to zero. We also check if the double of the current element is present in the set. If it is, we know that there are three elements that sum to zero.

If we find such a triple, we return true. If we don't find any, we return false.

The time complexity of this solution is O(n), where n is the size of the input list. This is because we iterate over the set once, and the operations we perform on the set (contains and add) take constant time.

The space complexity is O(n), where n is the size of the input list. This is because we store the elements of the list in a set. In the worst case, the set can contain all the elements of the list.