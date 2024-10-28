        List<Integer> result = new ArrayList<>();
        int min = Collections.min(lst);
        int max = Collections.max(lst);
        lst.remove(min);
        lst.remove(max);

        while (lst.size() != 0) {
            int min_of_rest = Collections.min(lst);
            result.add(min_of_rest);
            lst.remove(min_of_rest);
        }
        result.add(min);
        result.add(max);

        return result;
    }
}

