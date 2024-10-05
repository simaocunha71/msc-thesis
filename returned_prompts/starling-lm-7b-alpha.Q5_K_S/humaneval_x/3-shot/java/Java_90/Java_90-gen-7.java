        if (lst.size() < 2) {
            return Optional.empty();
        }
        List<Integer> sorted = new ArrayList<>(lst);
        Collections.sort(sorted);
        return Optional.of(sorted.get(1));
    }
}

