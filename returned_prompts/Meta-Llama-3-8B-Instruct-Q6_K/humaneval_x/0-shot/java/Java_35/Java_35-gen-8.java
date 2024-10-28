public int maxElement(List<Integer> l) {
    int max = l.get(0);
    for (int i = 1; i < l.size(); i++) {
        if (l.get(i) > max) {
            max = l.get(i);
        }
    }
    return max;
}

This solution iterates over the list and keeps track of the maximum element found so far. The maximum element is updated whenever a greater element is found. At the end of the iteration, the maximum element is returned.

The time complexity is O(n), where n is the size of the list, because we need to iterate over the entire list once. The space complexity is O(1), because we only use a constant amount of space to store the maximum element. 

The provided unit tests demonstrate that this solution works correctly for both small and large lists.