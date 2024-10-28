        List<Integer> result = new ArrayList<>();
        int max = Integer.MIN_VALUE;
        for (int n : numbers) {
            max = Math.max(max, n);
            result.add(max);
        }
        return result;
    }
}

