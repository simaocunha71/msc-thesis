        Collections.sort(lst);
        List<Integer> result = new ArrayList<>();

        int i = 0;
        while (i < lst.size()) {
            result.add(lst.get(i));
            int j = lst.size() - 1;
            while (j > i && lst.get(j) == lst.get(j - 1)) {
                j -= 1;
            }
            i = j;
        }
        return result;
    }
}



```