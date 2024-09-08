    sort(arr.begin(),arr.end(), [](int a, int b) {
        if (countBits(a) == countBits(b)) {
            return a < b;
        }
        return countBits(a) < countBits(b);
    });
    return arr;
}

int countBits(int n) {
    int count = 0;
    while (n) {
        n &= (n - 1);
        count++;
    }
    return count;
}
