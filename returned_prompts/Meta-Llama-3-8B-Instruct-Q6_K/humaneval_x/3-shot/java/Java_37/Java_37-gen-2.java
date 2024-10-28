        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 2 == 0) {
                List<Integer> even_numbers = new ArrayList<>();
                for (int j = 0; j < l.size(); j++) {
                    if (j % 2 == 0) {
                        even_numbers.add(l.get(j));
                    }
                }
                Collections.sort(even_numbers);
                result.add(even_numbers.get(0));
            } else {
                result.add(l.get(i));
            }
        }
        return result;
    }
}