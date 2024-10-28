        List<Integer> result = new ArrayList<>();
        result.add(0);
        result.add(0);

        for (int i = 1; i <= n; i++) {
            String s = Integer.toString(i);
            if (s.equals(new StringBuilder(s).reverse().toString())) {
                if (i % 2 == 0) {
                    result.set(0, result.get(0) + 1);
                } else {
                    result.set(1, result.get(1) + 1);
                }
            }
        }
        return result;

    }
}

