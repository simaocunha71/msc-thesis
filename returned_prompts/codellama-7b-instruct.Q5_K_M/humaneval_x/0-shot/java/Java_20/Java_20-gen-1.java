        List<Double> closest = new ArrayList<>();
        double minDiff = Double.MAX_VALUE;

        double min = numbers.get(0);
        double max = numbers.get(0);
        for (Double number: numbers) {
            if (number < min) min = number;
            if (number > max) max = number;
        }

        for (Double number: numbers) {
            double diff = Math.abs(max - number) - Math.abs(min - number);
            if (diff < minDiff) {
                minDiff = diff;
                closest.clear();
                closest.add(min);
                closest.add(max);
            } else if (diff == minDiff) {
                closest.add(number);
            }
        }

        closest.sort((o1, o2) -> o1.compareTo(o2));

        return closest;
    }
}
