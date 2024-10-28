        Collections.sort(numbers);
        double range = numbers.get(numbers.size() - 1) - numbers.get(0);

        for (int i = 0; i < numbers.size(); i++) {
            numbers.set(i, (numbers.get(i) - numbers.get(0)) / range);
        }
        return numbers;
    }
}

