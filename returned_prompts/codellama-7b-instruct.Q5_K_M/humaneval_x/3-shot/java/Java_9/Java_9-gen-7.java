        List<Integer> result = new ArrayList<>();
        int current_max = numbers.get(0);

        for (int n : numbers) {
            current_max = Math.max(current_max, n);
            result.add(current_max);
        }
        return result;
    }
}

