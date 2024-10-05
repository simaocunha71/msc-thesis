public boolean isSorted(List<Integer> lst) {
    int duplicates = 0;
    for (int i = 0; i < lst.size() - 1; i++) {
        if (lst.get(i) > lst.get(i + 1)) {
            return false;
        }
        if (lst.get(i).equals(lst.get(i + 1))) {
            duplicates++;
        }
    }
    return duplicates < 2;
}