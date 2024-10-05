public int doubleTheDifference(List<Object> lst) {
    int sum = 0;
    for (Object obj : lst) {
        if (obj instanceof Integer && (Integer)obj % 2 != 0) {
            sum += (Integer)obj * (Integer)obj;
        }
    }
    return sum;
}