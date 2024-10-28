        Collections.sort(lst);
        if (lst.size() < 2) return Optional.empty();
        return Optional.of(lst.get(1));
    }
}

