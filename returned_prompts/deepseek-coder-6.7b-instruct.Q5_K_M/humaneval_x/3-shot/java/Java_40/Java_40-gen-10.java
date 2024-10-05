        Set<Integer> set = new HashSet<>(l);

        for (int i = 0; i < l.size() - 2; i++) {
            for (int j = i + 1; j < l.size() - 1; j++) {
                for (int k = j + 1; k < l.size(); k++) {
                    if (set.contains(-(l.get(i) + l.get(j) + l.get(k)))) {
                        return true;
                    }
                }
            }
        }

        return false;
    }
}

