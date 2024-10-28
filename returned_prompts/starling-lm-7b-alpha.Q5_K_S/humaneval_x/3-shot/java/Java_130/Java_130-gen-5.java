        List<Integer> result = new ArrayList<>();
        if (n == 1) {
            result.add(3);
        } else if (n == 0) {
            return result;
        } else {
            result.add(3);
            result.add(1);
            result.add(2);
            for (int i = 3; i <= n; i++) {
                result.add(result.get(result.size() - 3) + result.get(result.size() - 2) + result.get(result.size() - 1));
            }
        }
        return result;
    }
}

