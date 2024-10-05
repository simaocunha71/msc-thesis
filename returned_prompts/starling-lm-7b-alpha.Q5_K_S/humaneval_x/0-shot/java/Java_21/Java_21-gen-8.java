        if (numbers == null || numbers.size() <= 1) {
            return numbers;
        }

        Collections.sort(numbers);
        double min = Math.max(0.0, numbers.get(0));
        double max = Math