public boolean pairsSumToZero(List<Integer> l) {
    // Sort the list in ascending order
    Collections.sort(l);

    // Initialize two pointers, one at the start and one at the end of the list
    int i = 0, j = l.size() - 1;

    // Iterate until the two pointers meet
    while (i < j) {
        // If the sum of the elements at the two pointers is zero, return true
        if (l.get(i) + l.get(j) == 0) {
            return true;
        }
        // If the sum of the elements at the two pointers is greater than zero,
        // move the right pointer to the left
        else if (l.get(i) + l.get(j) > 0) {
            j--;
        }
        // If the sum of the elements at the two pointers is less than zero,
        // move the left pointer to the right
        else {
            i++;
        }
    }

    // If no two elements sum to zero, return false
    return false;
}