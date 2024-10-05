        List<Integer> result = new ArrayList<>();
        while (n != 1) {
            if (n % 2 == 1) {
                result.add(n);
            }
            n = n % 2 == 0 ? n / 2 : n * 3 + 1;
        }
        result.add(1);
        Collections.sort(result);
        return result;
    }
}

