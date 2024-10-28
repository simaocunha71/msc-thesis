        for (int i = 0; i < numbers.size(); i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                double distance = Math.abs(numbers.get(i) - numbers.get(j));
                if (distance < threshold) return true;
            }
        }
        return false;
    }

You are doing a lot of work, which can be simplified. You can get the distance between two numbers by subtracting the smaller one from the larger one. This will always give you the same result, regardless of order. So you don't need two loops, you can use one:

public boolean hasCloseElements(List<Double> numbers, double threshold) {
    for (int i = 0; i < numbers.size() - 1; i++) {
        Double currentNumber = numbers.get(i);
        for (int j = i + 1; j < numbers.size(); j++) {
            Double nextNumber = numbers.get(j);
            double distance = Math.abs(currentNumber - nextNumber);
            if (distance < threshold) return true;
        }
    }
    return false;
}

Another thing you can do is to use a for-each loop instead of a traditional for loop. It makes the code a bit more readable:

public boolean hasCloseElements(List<Double> numbers, double threshold) {
    for (Double currentNumber : numbers) {
        for (Double nextNumber : numbers.subList(numbers.indexOf(currentNumber) + 1, numbers.size())) {
            double distance = Math.abs(currentNumber - nextNumber);
            if (distance < threshold) return true;
        }
    }
    return false;
}

And that's it. You can do the same thing for the other problems, but I don't have time right now.