        Collections.sort(numbers);
        double min_num = numbers.get(0);
        double max_num = numbers.get(numbers.size() - 1);
        double range = max_num - min_num;

        List<Double> result = new ArrayList<>();
        for (double num : numbers) {
            double rescaled_num = (num - min_num) / range;
            result.add(rescaled_num);
        }
        return result;
    }
}

