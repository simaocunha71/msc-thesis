        List<Integer> result = new ArrayList<>();
        if (n % 2 == 0) {
            result.add(n);
        } else {
            result.add(n);
            result.add(3 * n + 1);
            if (n % 2 == 0) {
                result.add(n / 2);
            }
        }
        while (result.get(result.size() - 1) != 1) {
            int last_result = result.remove(result.size() - 1);
            if (last_result % 2 == 0) {
                result.add(last_result / 2);
            } else {
                result.add(last_result * 3 + 1);
            }
        }
        Collections.sort(result);
        return result;
    }
}

