    string binary = "";
    int sum = 0;
    while(N){
        sum += N%10;
        N /= 10;
    }
    while(sum){
        binary = to_string(sum%2) + binary;
        sum /= 2;
    }
    return binary;
}

