        List<Integer> result = new ArrayList<>();
        if (lst.isEmpty()) {
            return result;
        }

        Integer min = lst.get(0);
        Integer max = lst.get(0);
        for (Integer value : lst) {
            if (value < min) {
                min = value;
            }
            if (value > max) {
                max = value;
            }
        }

        result.add(min);
        lst.remove(min);
        result.add(max);
        lst.remove(max);

        while (!lst.isEmpty()) {
            Integer value = lst.get(0);
            result.add(value);
            lst.remove(value);
        }

        return result;
    }
}
