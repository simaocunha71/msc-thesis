    sort(arr.begin(), arr.end(), [](int a, int b)
    {
        int count_a = 0, count_b = 0;
        while (a > 0) {
            a /= 2;
            count_a += a % 2;
        }
        while (b > 0) {
            b /= 2;
            count_b += b % 2;
        }
        if (count_a != count_b) {
            return count_a < count_b;
        }
        return a < b;
    });
    return arr;
}