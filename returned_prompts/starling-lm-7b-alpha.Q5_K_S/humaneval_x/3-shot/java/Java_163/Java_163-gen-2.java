        List<Integer> result = new ArrayList<>();
        for (int i = a; i <= b; i++) {
            int number = i;
            while (number > 0) {
                int digit = number % 10;
                if (digit % 2 == 0) {
                    result.add(digit);
                }
                number /= 10;
            }
        }
        return result;
    }
}

