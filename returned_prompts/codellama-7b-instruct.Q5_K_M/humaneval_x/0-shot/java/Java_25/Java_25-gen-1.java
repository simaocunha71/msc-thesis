        List<Integer> list = new ArrayList<>();
        for (int i = 2; i <= Math.sqrt(n); i++) {
            int count = 0;
            while (n % i == 0) {
                count++;
                n /= i;
            }
            if (count > 0) {
                for (int j = 0; j < count; j++) {
                    list.add(i);
                }
            }
        }
        if (n != 1) {
            list.add(n);
        }
        return list;
    }
}

