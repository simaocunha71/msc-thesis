        List<Integer> result = new ArrayList<>();
        int number = n;
        for (int i = 1; i <= n; i++) {
            result.add(number);
            if (i % 2 == 0) {
                number += 2;
            } else {
                number += 1;
            }
        }
        return result;
    }
}

