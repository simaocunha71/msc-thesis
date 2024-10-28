        double min 		= Collections.min(numbers);
        double max 		= Collections.max(numbers);
        double range 		= max - min;
        List<Double> rescaled = new ArrayList<Double>();

        for (double num : numbers) {
            rescaled.add((num - min) / range);
        }

        return rescaled;
     }
}

