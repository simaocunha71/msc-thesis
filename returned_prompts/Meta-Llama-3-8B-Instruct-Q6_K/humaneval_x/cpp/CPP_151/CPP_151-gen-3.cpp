    long long sum = 0;
    for (float num : lst) {
        if (num > 0 && num == floor(num)) {
            sum += pow(num, 2);
        }
    }
    return sum;
}
