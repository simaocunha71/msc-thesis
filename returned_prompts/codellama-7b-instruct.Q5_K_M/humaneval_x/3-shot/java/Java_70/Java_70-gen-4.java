        List<Integer> result = new ArrayList<>();
        Collections.sort(lst);
        int min = lst.get(0);
        result.add(min);
        int max = lst.get(lst.size() - 1);
        result.add(max);
        lst.remove(min);
        lst.remove(max);
        while (!lst.isEmpty()) {
            int min_rem = Collections.min(lst);
            result.add(min_rem);
            lst.remove(min_rem);
            int max_rem = Collections.max(lst);
            result.add(max_rem);
            lst.remove(max_rem);
        }
        return result;
    }
}

