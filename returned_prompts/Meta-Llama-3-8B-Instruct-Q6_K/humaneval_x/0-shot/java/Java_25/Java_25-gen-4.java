        List<Integer> result = new ArrayList<Integer>();

        for (int i = 2; i <= n; i++) {
            int count = 0;
            while (n % i == 0) {
                n = n / i;
                count++;
            }
            if (count > 0) {
                for (int j = 0; j < count; j++) {
                    result.add(i);
                }
            }
        }
        return result;
    }

