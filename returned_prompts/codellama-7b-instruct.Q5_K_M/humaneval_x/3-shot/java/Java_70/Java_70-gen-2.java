        List<Integer> result = new ArrayList<>();
        int min = Collections.min(lst);
        int max = Collections.max(lst);

        while (lst.contains(min)) {
            result.add(min);
            lst.remove(Integer.valueOf(min));
        }
        result.add(max);
        lst.remove(Integer.valueOf(max));

        while (lst.size() > 0) {
            min = Collections.min(lst);
            result.add(min);
            lst.remove(Integer.valueOf(min));
        }
        return result;
    }
}

