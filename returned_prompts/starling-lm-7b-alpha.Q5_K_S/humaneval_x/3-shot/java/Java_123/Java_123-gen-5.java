        List<Integer> result = new ArrayList<>();
        result.add(1);
        while (n != 1) {
            if (n % 2 == 1) {
                result.add(n);
                if (n == 1) break;
                n = 3 * n + 1;
            } else {
                result.add(n);
                n /= 2;
            }
        }
        Collections.sort(result);
        return result;
    }
}

