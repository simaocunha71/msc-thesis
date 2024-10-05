        double min = Collections.min(numbers);
        double max = Collections.max(numbers);
        List<Double> result = new ArrayList<>();
        for (Double number : numbers) {
            result.add((number - min) / (max - min));
        }
        return result;
    }
}

The problem with this code is that it throws an exception if the input list is empty. It will fail when trying to find min and max, because there are no elements in the list.

