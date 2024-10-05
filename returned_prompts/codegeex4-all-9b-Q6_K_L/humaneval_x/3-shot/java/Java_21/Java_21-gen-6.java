        double min = Collections.min(numbers);
        double max = Collections.max(numbers);
        double range = max - min;

        for (int i = 0; i < numbers.size(); i++) {
            numbers.set(i, (numbers.get(i) - min) / range);
        }
        return numbers;
    }
}

