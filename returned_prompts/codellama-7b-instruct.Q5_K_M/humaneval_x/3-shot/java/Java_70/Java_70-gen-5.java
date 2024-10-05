        List<Integer> result = new ArrayList<>();

        if (lst.isEmpty()) return result;

        int min = lst.get(0);
        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i) < min) min = lst.get(i);
        }
        result.add(min);
        lst.remove(min);

        int max = lst.get(0);
        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i) > max) max = lst.get(i);
        }
        result.add(max);
        lst.remove(max);

        while (!lst.isEmpty()) {
            min = lst.get(0);
            for (int i = 1; i < lst.size(); i++) {
                if (lst.get(i) < min) min = lst.get(i);
            }
            result.add(min);
            lst.remove(min);
        }

        return result;
    }
}

