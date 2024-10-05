        List<Integer> result = new ArrayList<>();
        Collections.sort(lst);
        int start = 0;
        while (start < lst.size()) {
            result.add(lst.get(start));
            int end = lst.size() - 1;
            while (end > start && lst.get(end) == lst.get(start)) {
                end--;
            }
            result.addAll(lst.subList(start + 1, end + 1));
            start = end + 1;
        }
        return result;
    }
}


```