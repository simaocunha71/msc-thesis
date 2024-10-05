        Set<Integer> set = new HashSet<>();
        for (Integer i : lst2) {
            set.add(i);
        }
        for (Integer i : lst1) {
            if (!set.contains(i % 2)) {
                return "NO";
            }
        }
        return "YES";
    }
}

