        if (lst.size() < 2) return Optional.empty();
        Collections.sort(lst);
        return Optional.of(lst.get(1));
    }
}

