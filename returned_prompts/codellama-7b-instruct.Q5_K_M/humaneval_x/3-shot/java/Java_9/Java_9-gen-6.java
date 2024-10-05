        List<Integer> result = new ArrayList<>();
        result.add(numbers.get(0));

        for (int i = 1; i < numbers.size(); i++) {
            int current_max = Math.max(result.get(i - 1), numbers.get(i));
            result.add(current_max);
        }
        return result;
    }
}

