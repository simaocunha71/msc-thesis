        if (lst.size() < 2) {
            return Optional.empty();
        }
        Collections.sort(lst);
        int smallest = lst.get(0);
        int secondSmallest = lst.get(1);
        if (secondSmallest == smallest) {
            return Optional.empty();
        }
        return Optional.of(secondSmallest);
    }
}

