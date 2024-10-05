        Set<Integer> freq = new HashSet<>();
        for (int i : lst) {
            freq.add(i);
        }

        for (int i = 1; i <= lst.size(); i++) {
            if (freq.contains(i) && freq.size() >= i) {
                return i;
            }
        }
        return -1;
    }
}

