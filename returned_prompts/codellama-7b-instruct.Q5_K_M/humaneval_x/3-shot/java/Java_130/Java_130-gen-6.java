        List<Integer> result = new ArrayList<>();
        result.add(3);
        result.add(1);
        result.add(2);
        for (int i = 3; i <= n; i++) {
            int last_number = result.get(result.size() - 1);
            if (i % 2 == 0) {
                result.add(i / 2);
            } else {
                result.add(last_number + result.get(i - 1) + result.get(i - 2));
            }
        }
        return result;
    }
}

