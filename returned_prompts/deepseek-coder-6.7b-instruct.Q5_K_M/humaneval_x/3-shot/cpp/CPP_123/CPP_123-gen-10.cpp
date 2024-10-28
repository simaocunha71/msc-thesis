    vector<int> oddNumbers;
    while (n != 1) {
        if (n % 2 != 0) {
            oddNumbers.push_back(n);
        }
        n = n % 2 ? n*3 + 1 : n / 2;
    }
    oddNumbers.push_back(1);
    sort(oddNumbers.begin(), oddNumbers.end());
    return oddNumbers;
}


