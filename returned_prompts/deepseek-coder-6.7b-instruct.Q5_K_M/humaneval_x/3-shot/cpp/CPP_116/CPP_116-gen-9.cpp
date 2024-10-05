    sort(arr.begin(), arr.end(), [](int a, int b){
        int bit_count_a = __builtin_popcount(abs(a));
        int bit_count_b = __builtin_popcount(abs(b));
        if(bit_count_a != bit_count_b)
            return bit_count_a < bit_count_b;
        else
            return a < b;
    });
    return arr;
}


