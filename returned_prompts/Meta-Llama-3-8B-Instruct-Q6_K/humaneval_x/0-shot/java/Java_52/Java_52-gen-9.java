Here is the solution in Java:
```
public boolean belowThreshold(List<Integer> l, int t) {
    for (int num : l) {
        if (num >= t) {
            return false;
        }
    }
    return true;
}
```
This solution iterates over the list of integers and checks if any of them are greater than or equal to the threshold. If it finds such a number, it immediately returns `false`. If it doesn't find any such numbers, it returns `true`. The time complexity of this solution is O(n), where n is the size of the list. The space complexity is O(1), since we're only using a constant amount of space to store the threshold and a few variables.