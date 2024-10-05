        List<Integer> result = new ArrayList<>();
        int next = 1;
        while (next <= n) {
            result.add(next);
            next += (next % 2 == 0) ? 2 : 1;
        }
        return result;
    }
}

