        List<Integer> result = new ArrayList<>();
        if (n == 0) return result;
        result.add(3);
        if (n == 1) return result;
        result.add(1);
        if (n == 2) return result;
        result.add(2);

        while (result.size() < n + 1) {
            int next = result.get(result.size() - 1) + result.get(result.size() - 2) + result.get(result.size() - 3);
            result.add(next);
        }
        return result;
    }
}

