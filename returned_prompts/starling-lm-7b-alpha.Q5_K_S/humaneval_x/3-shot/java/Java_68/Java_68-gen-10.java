        List<Integer> result = null;
        List<Integer> even_values = new ArrayList<>();

        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) % 2 == 0) {
                even_values.add(i);
            }
        }

        if (even_values.size() > 0) {
            result = new ArrayList<>();
            result.add(even_values.get(0));
            result.add(arr.get(even_values.get(0)));
        }

        return result;
    }
}

