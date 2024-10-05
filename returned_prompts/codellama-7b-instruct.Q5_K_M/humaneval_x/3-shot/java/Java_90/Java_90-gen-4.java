        if (lst.size() < 2) {
            return Optional.empty();
        }
        lst.sort(Comparator.naturalOrder());
        return Optional.of(lst.get(1));
    }
}

