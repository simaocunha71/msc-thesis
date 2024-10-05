    public boolean isSorted(List<Integer> lst) {
        if (lst.size() <= 1) {
            return true;
        }

        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i - 1) >= lst.get(i)) {
                return false;
            }
        }

        return true;
    }  // Time Complexity: O(n), Space Complexity: O(1) where n is the number of elements in the list.