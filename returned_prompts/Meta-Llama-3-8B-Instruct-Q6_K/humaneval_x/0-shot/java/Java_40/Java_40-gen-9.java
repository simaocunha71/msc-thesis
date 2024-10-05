    public boolean triplesSumToZero(List<Integer> l) {
        Set<Integer> set = new HashSet<>();
        for (int i : l) {
            set.add(i);
        }
        
        for (int i : set) {
            for (int j : set) {
                if (set.contains(-i - j)) {
                    return true;
                }
            }
        }
        return false;
    }