        if (lst.size() < 2) return Optional.empty();
        Set<Integer> set = new HashSet<>(lst);
        int min = Collections.min(set);
        set.remove(min);
        return set.stream().min(Integer::compareTo);
    }
}

