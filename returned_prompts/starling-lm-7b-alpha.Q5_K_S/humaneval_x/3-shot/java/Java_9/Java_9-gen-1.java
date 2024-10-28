        List<Integer> result = new ArrayList<>();
        int max = Integer.MIN_VALUE;
        for (int n : numbers) {
            max = Math.max(n, max);
            result.add(max);
        }
        return result;
    }
}

