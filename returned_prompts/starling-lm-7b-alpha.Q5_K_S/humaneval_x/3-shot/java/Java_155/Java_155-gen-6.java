        List<Integer> result = new ArrayList<>();
        int evens = 0;
        int odds = 0;
        while (num != 0) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                evens += 1;
            } else {
                odds += 1;
            }
            num /= 10;
        }
        result.add(evens);
        result.add(odds);
        return result;
    }
}

