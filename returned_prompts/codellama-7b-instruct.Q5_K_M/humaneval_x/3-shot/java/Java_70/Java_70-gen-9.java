        List<Integer> result = new ArrayList<>();
        int min_val = Collections.min(lst);
        int max_val = Collections.max(lst);

        while (!lst.isEmpty()) {
            if (lst.contains(min_val)) {
                result.add(min_val);
                lst.remove(Integer.valueOf(min_val));
            }
            if (lst.contains(max_val)) {
                result.add(max_val);
                lst.remove(Integer.valueOf(max_val));
            }
        }
        return result;
    }
}

