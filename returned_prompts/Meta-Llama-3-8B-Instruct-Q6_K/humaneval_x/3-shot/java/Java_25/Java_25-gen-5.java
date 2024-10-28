        List<Integer> result = new ArrayList<>();
        int current = 2;

        while (n > 1) {
            int count = 0;
            while (n % current == 0) {
                n /= current;
                count++;
            }
            if (count > 0) {
                for (int i = 0; i < count; i++) {
                    result.add(current);
                }
            }
            current++;
        }
        return result;
    }
}

