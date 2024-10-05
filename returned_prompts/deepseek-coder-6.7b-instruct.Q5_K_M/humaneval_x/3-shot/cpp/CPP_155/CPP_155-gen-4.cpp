    vector<int> counts(2, 0); // [even, odd]
    num = abs(num);
    while(num){
        int digit = num % 10;
        if (digit % 2 == 0)
            counts[0]++;
        else
            counts[1]++;
        num /= 10;
    }
    return counts;
}


