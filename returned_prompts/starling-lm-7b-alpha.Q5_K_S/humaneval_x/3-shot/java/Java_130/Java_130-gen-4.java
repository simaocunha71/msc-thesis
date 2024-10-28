        List<Integer> result = new ArrayList<>();
        result.add(3);

        int[] fib = new int[n + 1];
        fib[1] = 1;
        for (int i = 2; i < fib.length; i++) {
            if (i % 2 == 0) {
                fib[i] = fib[i - 1];
            } else {
                fib[i] = fib[i - 1] + fib[i - 2] + fib[i + 1];
            }
            result.add(fib[i]);
        }
        return result;
    }
}

