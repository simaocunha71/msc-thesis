        int secondSmallest = -1;

        for (int i = 0; i < lst.size(); i++) {
            if (lst.get(i) < secondSmallest || secondSmallest == -1) {
                secondSmallest = lst.get(i);
            }
        }
        if (secondSmallest == -1) {
            return Optional.empty();
        } else {
            return Optional.of(secondSmallest);
        }
    }
}

