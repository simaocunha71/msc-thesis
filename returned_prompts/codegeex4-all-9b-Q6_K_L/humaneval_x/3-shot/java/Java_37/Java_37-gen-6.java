        List<Integer> result = new ArrayList<>();

        List<Integer> even_indicies = new ArrayList<>();
        for (int i = 0; i < l.size(); i += 2) {
            even_indicies.add(l.get(i));
        }
        Collections.sort(even_indicies);

        for (int i = 0; i < l.size(); i++) {
            if (i % 2 == 0) {
                result.add(even_indicies.get(i / 2));
            } else {
                result.add(l.get(i));
            }
        }
        return result;
    }
}

