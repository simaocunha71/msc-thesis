public int sumSquares(List<Double> lst) {
    return (int) Math.ceil(lst.stream().mapToDouble(Math::ceil).map(Math::pow).sum());
}