public boolean belowThreshold(List<Integer> l, int t) {
    for (Integer i : l) {
        if (i >= t) {
            return false;
        }
    }
    return true;
}