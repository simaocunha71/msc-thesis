        if (lst.size() < 2) return Optional.empty();
        Set<Integer> set = new HashSet<>(lst);
        Integer smallest = Collections.min(set);
        set.remove(smallest);
        return set.stream().map(i -> i < smallest ? i : null).filter(i -> i != null).findFirst();
    }
}

