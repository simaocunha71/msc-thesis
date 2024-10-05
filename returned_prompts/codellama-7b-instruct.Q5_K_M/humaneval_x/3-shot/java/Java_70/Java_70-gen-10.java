        List<Integer> result = new ArrayList<>();

        if (lst.isEmpty()) return result;

        int min = lst.get(0);
        int max = lst.get(0);

        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i) < min) min = lst.get(i);
            if (lst.get(i) > max) max = lst.get(i);
        }

        for (int i = min; i <= max; i++) {
            if (lst.contains(i)) result.add(i);
        }
        return result;
    }
}

