    int sum = 0;
    for (int i = 1; i < lst.size(); i++) {
        if (i % 2 == 0 && lst.get(i) % 2 != 0) {
            sum += lst.get(i);
        }
    }
    return sum;
}