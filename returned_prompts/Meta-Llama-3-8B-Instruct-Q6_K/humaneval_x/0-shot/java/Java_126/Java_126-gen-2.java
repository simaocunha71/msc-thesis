    public boolean isSorted(List<Integer> lst) {
        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i - 1) >= lst.get(i)) {
                return false;
            }
        }
        return true;
    } 

