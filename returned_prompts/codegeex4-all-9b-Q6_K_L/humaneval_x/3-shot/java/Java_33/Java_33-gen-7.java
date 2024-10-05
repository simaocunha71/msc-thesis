        List<Integer> result = new ArrayList<>(l);
        List<Integer> to_sort = new ArrayList<>();

        for (int i = 0; i < l.size(); i += 3) {
            to_sort.add(l.get(i));
        }

        Collections.sort(to_sort);
        for (int i = 0; i < to_sort.size(); i++) {
            result.set(i * 3, to_sort.get(i));
        }

        return result;
    }
}

