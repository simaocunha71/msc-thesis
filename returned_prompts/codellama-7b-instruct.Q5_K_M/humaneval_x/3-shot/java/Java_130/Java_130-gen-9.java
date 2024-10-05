        List<Integer> result = new ArrayList<>();
        result.add(1);
        result.add(3);
        result.add(2);
        result.add(8);
        if (n == 0) return result;

        for (int i = 0; i < n; i++) {
            int new_number = 1 + result.get(i) + result.get(i + 1);
            result.add(new_number);
        }
        return result;
    }
}

