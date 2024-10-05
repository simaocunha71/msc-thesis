        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < l.size(); i++) {
            if (set.contains(-l.get(i))) return true;
            set.add(l.get(i));
        }
        return false;
    }
}

