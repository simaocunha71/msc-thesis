        List<Integer> result = new ArrayList<>();
        int current_max = Integer.MIN_VALUE;

        for (int num : numbers) {
            current_max = Math.max(current_max, num);
            result.add(current_max);
        }
        return result;
    }
}

