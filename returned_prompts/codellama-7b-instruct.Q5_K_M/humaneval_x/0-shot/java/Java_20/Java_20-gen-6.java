        Collections.sort(numbers);
        List<Double> output = new ArrayList<Double>();
        int index = 0;
        for (int i = 1; i < numbers.size(); i++) {
            if (Math.abs(numbers.get(i) - numbers.get(index)) < Math.abs(numbers.get(i) - numbers.get(i + 1))) {
                index = i;
            }
        }
        output.add(numbers.get(index));
        output.add(numbers.get(index + 1));
        return output;
    }
}
