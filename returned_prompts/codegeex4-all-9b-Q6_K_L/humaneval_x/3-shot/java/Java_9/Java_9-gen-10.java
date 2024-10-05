        List<Integer> result = new ArrayList<>();
        int max = Integer.MIN_VALUE;

        for (int number : numbers) {
            max = Math.max(max, number);
            result.add(max);
        }
        return result;
    }
}

