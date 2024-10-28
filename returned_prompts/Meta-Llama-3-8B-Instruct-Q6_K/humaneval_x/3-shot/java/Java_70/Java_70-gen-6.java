        if (lst.size() <= 1) return lst;

        List<Integer> result = new ArrayList<>();
        List<Integer> minMax = new ArrayList<>();

        while (lst.size() > 0) {
            int min = Collections.min(lst);
            int max = Collections.max(lst);

            result.add(min);
            lst.remove((Integer) min);

            if (lst.size() > 0) {
                result.add(max);
                lst.remove((Integer) max);
            }

            minMax = lst;
        }

        return result;
    }
}