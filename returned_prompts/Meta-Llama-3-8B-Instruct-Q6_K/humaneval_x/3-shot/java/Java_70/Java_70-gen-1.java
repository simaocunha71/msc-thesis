        if (lst.size() == 0) {
            return lst;
        }

        List<Integer> result = new ArrayList<>();
        List<Integer> min_max = new ArrayList<>();

        while (!lst.isEmpty()) {
            int min = Integer.MAX_VALUE;
            int max = Integer.MIN_VALUE;
            for (int i : lst) {
                if (i < min) {
                    min = i;
                } else if (i > max) {
                    max = i;
                }
            }
            result.add(min);
            lst.remove((Integer) min);
            min_max.add(max);
            lst.remove((Integer) max);
        }
        result.addAll(min_max);
        return result;
    }
}

