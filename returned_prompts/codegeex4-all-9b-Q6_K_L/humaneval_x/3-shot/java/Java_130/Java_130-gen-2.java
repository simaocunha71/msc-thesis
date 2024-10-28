        List<Integer> result = new ArrayList<>();
        result.add(1);
        result.add(3);
        result.add(2);

        for (int i = 3; i <= n; i++) {
            result.add(result.get(i - 1) + result.get(i - 2) + result.get(i - 3));
        }
        return result;
    }
}

