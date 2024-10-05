        if (lst.size() < 2) {
            return Optional.empty();
        }

        int first = lst.get(0);
        int second = lst.get(1);

        for (int i = 2; i < lst.size(); i++) {
            if (lst.get(i) < second) {
                second = lst.get(i);
            }
        }

        return Optional.of(second);
    }
}

