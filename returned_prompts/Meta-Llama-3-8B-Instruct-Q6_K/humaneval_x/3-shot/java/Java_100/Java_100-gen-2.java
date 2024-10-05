        List<Integer> result = new ArrayList<>();
        int current = n;
        while (n > 0) {
            if (n % 2 == 1) {
                result.add(0, current);
                current += 2;
            } else {
                result.add(0, current);
                current += 1;
            }
            n -= 1;
        }
        return result;
    }
}

