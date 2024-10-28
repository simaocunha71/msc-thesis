        List<Integer> list = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
            String s = String.valueOf(i);
            if (s.equals(new StringBuilder(s).reverse().toString())) {
                if (i % 2 == 0) {
                    list.add(i);
                } else {
                    list.add(i);
                    list.add(i);
                }
            }
        }

        return list;
    }
}


