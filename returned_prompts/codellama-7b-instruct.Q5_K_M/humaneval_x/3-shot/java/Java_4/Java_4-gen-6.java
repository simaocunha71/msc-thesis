        double sum = 0.0;

        for (double number : numbers) {
            sum += Math.abs(number - numbers.get(numbers.size() / 2));
        }
        return sum / numbers.size();
    }
}

