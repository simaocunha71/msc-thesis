    string binary_sum = "";
    int remainder;
    while(N > 0){
        remainder = N % 2;
        N = N / 2;
        binary_sum = to_string(remainder) + binary_sum;
    }
    return binary_sum;
}


