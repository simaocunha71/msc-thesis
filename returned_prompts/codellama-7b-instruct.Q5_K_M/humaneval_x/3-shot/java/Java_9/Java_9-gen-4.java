        List<Integer> result = new ArrayList<>();

        if (numbers.size() == 0) return result;

        int current_max = numbers.get(0);

        for (int number : numbers) {
            current_max = Math.max(current_max, number);
            result.add(current_max);
        }

        return result;
    }
}

