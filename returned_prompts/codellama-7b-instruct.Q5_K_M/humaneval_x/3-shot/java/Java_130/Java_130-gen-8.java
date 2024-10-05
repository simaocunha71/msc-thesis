        List<Integer> result = new ArrayList<>();
        result.add(1);
        result.add(3);
        result.add(2);

        for (int i = 3; i <= n; i++) {
            if (i % 2 == 0) {
                result.add((int) Math.round(((double) i / 2) + 1));
            } else {
                int a = result.get(result.size() - 3);
                int b = result.get(result.size() - 2);
                int c = result.get(result.size() - 1);
                result.add(a + b + c);
            }
        }
        return result;
    }
}

