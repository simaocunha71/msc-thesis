        List<Integer> result = new ArrayList<>(l);
        List<Integer> to_sort = new ArrayList<>();

        for (int i = 0; i < result.size(); i++) {
            if (i % 3 == 0) {
                to_sort.add(result.get(i));
            }
        }

        Collections.sort(to_sort);

        for (int i = 0; i < result.size(); i++) {
            if (i % 3 == 0) {
                result.set(i, to_sort.remove(0));
            }
        }

        return result;
    }
}

