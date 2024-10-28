        Set<Integer> set = new HashSet<>(l);
        for (int i = 0; i < l.size(); i++) {
            for (int j = i + 1; j < l.size(); j++) {
                int t = -(l.get(i) + l.get(j));
                if (set.contains(t)) return true;
            }
        }
        return false;
    }
}

