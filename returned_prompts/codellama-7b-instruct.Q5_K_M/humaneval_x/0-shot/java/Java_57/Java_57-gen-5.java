        int count = l.size();
        if (count < 2) {
            return true;
        }

        for (int i = 0; i < count - 1; i++) {
            if (l.get(i) == l.get(i + 1)) {
                continue;
            }

            if (l.get(i) > l.get(i + 1)) {
                for (int j = i + 1; j < count - 1; j++) {
                    if (l.get(j) > l.get(j + 1)) {
                        continue;
                    } else {
                        return false;
                    }
                }
            } else {
                for (int j = i + 1; j < count - 1; j++) {
                    if (l.get(j) < l.get(j + 1)) {
                        continue;
                    } else {
                        return false;
                    }
                }
            }
        }
        return true;
    }

    /**
    Return True if list elements are pairwise distinct.
    >>> distinct(Arrays.asList(1, 2, 3, 4))
    true
    >>> distinct(Arrays.asList(1, 2, 3, 2))
    false
     */
    public boolean distinct(List<Integer> l) {
        int count = l.size();
        for (int i = 0; i < count - 1; i++) {
            for (int j = i + 1; j < count; j++) {
                if (l.get(i) == l.get(j)) {
                    return false;
                }
            }
        }
        return true;
    }

    /**
    Return True if list elements are pairwise unequal.
    >>> unequal(Arrays.asList(1, 2, 3, 4))
    true
    >>> unequal(Arrays.asList(1, 1, 2, 2))
    false
     */
    public boolean unequal(List<Integer> l) {
        int