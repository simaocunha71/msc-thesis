        List<Integer> result = new ArrayList<>(l);
        List<Integer> to_sort = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 3 == 0) {
                to_sort.add(l.get(i));
            }
        }
        Collections.sort(to_sort);
        int index = 0;
        for (int i = 0; i < l.size(); i++) {
            if (i % 3 == 0) {
                result.set(i, to_sort.get(index));
                index += 1;
            }
        }
        return result;
    }
}

