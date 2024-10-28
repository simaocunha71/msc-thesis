        List<Integer> result = new ArrayList<>();
        int current = 2;
        while (n > 1) {
            while (n % current == 0) {
                n /= current;
                result.add(current);
            }
            current += 1;
        }
        return result;
    }
}

