        int even_palindromes = 0;
        int odd_palindromes = 0;
        for (int i = 1; i <= n; i++) {
            int number = i;
            while (number != 0) {
                int digit = number % 10;
                if (digit != 0) {
                    number /= 10;
                } else {
                    break;
                }
            }
            if (number == 0) {
                if (i % 2 == 0) {
                    even_palindromes += 1;
                } else {
                    odd_palindromes += 1;
                }
            }
        }
        List<Integer> result = new ArrayList<>();
        result.add(even_palindromes);
        result.add(odd_palindromes);
        return result;
    }
}

