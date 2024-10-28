        List<Integer> result = new ArrayList<>();
        for (int i = a; i <= b; i++) {
            int n = i;
            while (n > 0) {
                int digit = n % 10;
                n /= 10;
                if (digit % 2 == 0) {
                    result.add(digit);
                }
            }
        }
        return result;
    }
}

