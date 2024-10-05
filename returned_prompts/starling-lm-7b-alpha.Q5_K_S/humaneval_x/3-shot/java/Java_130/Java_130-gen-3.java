        List<Integer> result = new ArrayList<>();
        if (n == 0) return result;
        if (n == 1) {
            result.add(3);
            return result;
        }
        if (n == 2) {
            result.add(3);
            result.add(1);
            return result;
        }
        result.add(3);
        result.add(1);
        result.add(2);

        while (result.size() <= n) {
            if (result.size() % 2 == 0) {
                result.add(result.size() / 2 + 1);
            } else {
                result.add(result.get(result.size() - 1) + result.get(result.size() - 2) + result.get(result.size() + 1));
            }
        }
        return result;
    }
}

