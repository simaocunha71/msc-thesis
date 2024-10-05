    string binary_sum = "";
    while(N > 0){
        binary_sum = to_string(N%2) + binary_sum;
        N = N/2;
    }
    return binary_sum;
}


