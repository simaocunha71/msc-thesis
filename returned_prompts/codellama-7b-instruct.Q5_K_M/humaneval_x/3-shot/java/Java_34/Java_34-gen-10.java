        List<Integer> result = new ArrayList<>(l);
        result.sort(Comparator.naturalOrder());

        int last = result.get(0);
        int index = 1;

        for (int i = 1; i < result.size(); i++) {
            if (result.get(i) != last) {
                result.set(index, result.get(i));
                last = result.get(i);
                index += 1;
            }
        }
        result.subList(index, result.size()).clear();

        return result;
    }
}

