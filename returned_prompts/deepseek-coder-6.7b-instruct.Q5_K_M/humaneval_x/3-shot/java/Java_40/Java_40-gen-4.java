        Set<Integer> set = new HashSet<>(l);

        for (int i = 0; i < l.size(); i++) {
            for (int j = i + 1; j < l.size(); j++) {
                if (set.contains(-(l.get(i) + l.get(j)))) {
                    return true;
                }
            }
        }

        return false;
    }
}

