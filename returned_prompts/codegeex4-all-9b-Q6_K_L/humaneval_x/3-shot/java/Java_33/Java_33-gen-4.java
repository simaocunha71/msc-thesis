        List<Integer> result = new ArrayList<>();
        List<Integer> sort = new ArrayList<>();

        for (int i = 0; i < l.size(); i++) {
            if (i % 3 == 0) {
                result.add(l.get(i));
            } else {
                sort.add(l.get(i));
            }
        }
        Collections.sort(sort);
        int j = 0;

        for (int i = 0; i < l.size(); i++) {
            if (i % 3 == 0) {
                result.set(i, l.get(i));
            } else {
                result.set(i, sort.get(j));
                j++;
            }
        }
        return result;

    }
}

