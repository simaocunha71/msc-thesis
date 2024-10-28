        if (lst.size() < 2) return Optional.empty();

        Set<Integer> set = new TreeSet<>(lst);
        return Optional.of(set.pollFirst());
    }
}

