        if (lst.size() < 2) {
            return Optional.empty();
        }
        List<Integer> sortedList = new ArrayList<>(lst);
        Collections.sort(sortedList);
        int firstSmallest = sortedList.get(0);
        for (int i = 1; i < sortedList.size(); i++) {
            if (sortedList.get(i) != firstSmallest) {
                return Optional.of(sortedList.get(i));
            }
        }
        return Optional.empty();
    }
}

