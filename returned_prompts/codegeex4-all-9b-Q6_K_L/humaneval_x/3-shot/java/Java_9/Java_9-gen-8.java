        List<Integer> result = new ArrayList<>();
        int current_max = Integer.MIN_VALUE;

        for (int i : numbers) {
            current_max = Math.max(current_max, i);
            result.add(current_max);
        }
        return result;
    }
}

