        for (int i = 2; i <= n; i++) {
            if (n % i == 0) {
                List<Integer> list = new ArrayList<>();
                while (n % i == 0) {
                    list.add(i);
                    n /= i;
                }
                return list;
            }
        }
        return Collections.singletonList(n);
    }
}
