        double min = numbers.get(0);
        double max = numbers.get(0);

        for (double number : numbers) {
            if (number < min) min = number;
            if (number > max) max = number;
        }

        List<Double> result = new ArrayList<>();

        for (double number : numbers) {
            result.add((number - min) / (max - min));
        }

        return result;
    }
}

