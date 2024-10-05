    public boolean isSorted(List<Integer> lst) {
        for (int i = 0; i < lst.size() - 1; i++) {
            if (lst.get(i) >= lst.get(i + 1)) {
                if (lst.indexOf(lst.get(i)) != lst.lastIndexOf(lst.get(i))) {
                    return false;
                }
            } else {
                return false;
            }
        }
        return true;
    }  // Time complexity O(n), where n is the size of the input list.
    // Space complexity O(1), as we are only using a constant amount of space.