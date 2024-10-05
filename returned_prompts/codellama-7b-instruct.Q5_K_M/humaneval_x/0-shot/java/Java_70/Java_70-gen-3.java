        List<Integer> result = new ArrayList<>();
        if (lst.size() == 0) {
            return result;
        }
        int min = Collections.min(lst);
        int max = Collections.max(lst);
        result.add(min);
        result.add(max);
        lst.remove(min);
        lst.remove(max);
        for (int i = 0; i < lst.size() / 2; i++) {
            result.add(lst.get(i));
            result.add(lst.get(lst.size() - 1 - i));
        }
        if (lst.size() % 2 != 0) {
            result.add(lst.get(lst.size() / 2));
        }
        return result;
    }
}