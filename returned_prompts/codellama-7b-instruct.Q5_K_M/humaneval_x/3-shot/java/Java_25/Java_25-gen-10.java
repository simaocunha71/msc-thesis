        List<Integer> result = new ArrayList<>();
        int i = 2;

        while (n > 1) {
            if (n % i == 0) {
                result.add(i);
                n /= i;
            } else {
                i += 1;
            }
        }
        return result;
    }
}

