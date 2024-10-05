public int doubleTheDifference(List<Object> lst) {
    int sumOfSquares = 0;
    int sumOfNumbers = 0;
    for (Object n : lst) {
        if (n instanceof Integer) {
            int x = (Integer) n;
            sumOfNumbers += x;
            sumOfSquares += x * x;
        }
    }
    return sumOfNumbers * sumOfNumbers - sumOfSquares;
}
