        List<Integer> result = new ArrayList<>();
        result.add(n);
        int current = n;
        while (n > 1) {
            n = n % 2 == 0 ? n - 1 : n + 1;
            result.add(n);
        }
        return result;
    }
}

