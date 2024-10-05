public int sumSquares(List<Double> lst) {
    int sum = 0;
    for (Double num : lst) {
        sum += Math.ceil(num) * Math.ceil(num);
    }
    return sum;
}
