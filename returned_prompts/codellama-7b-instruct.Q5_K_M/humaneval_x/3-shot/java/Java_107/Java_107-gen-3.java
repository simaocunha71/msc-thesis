        List<Integer> result = new ArrayList<>();
        int even = 0;
        int odd = 0;

        for (int i = 1; i < n; i++) {
            String s = Integer.toString(i);
            if (s.equals(new StringBuilder(s).reverse().toString())) {
                if (i % 2 == 0) even += 1;
                else odd += 1;
            }
        }
        result.add(even);
        result.add(odd);
        return result;
    }
}

