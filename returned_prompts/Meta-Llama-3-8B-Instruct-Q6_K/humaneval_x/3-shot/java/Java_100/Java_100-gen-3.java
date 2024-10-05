        List<Integer> result = new ArrayList<>();
        int current = n;
        while (n > 0) {
            if (n % 2 == 0) {
                result.add(0, current);
                n -= 1;
            } else {
                result.add(0, current);
                n -= 2;
            }
            current += 1;
        }
        return result;
    }
}

