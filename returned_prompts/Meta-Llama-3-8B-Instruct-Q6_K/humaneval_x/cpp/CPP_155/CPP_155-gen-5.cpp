    vector<int> res;
    num = abs(num);
    int even = 0, odd = 0;
    while(num > 0) {
        int digit = num % 10;
        if(digit % 2 == 0) even++;
        else odd++;
        num /= 10;
    }
    res.push_back(even);
    res.push_back(odd);
    return res;
}

