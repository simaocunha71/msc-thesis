    string binary;
    int i;
    for (i=0;i<N;i++){
        int rem = N%2;
        binary=to_string(rem)+binary;
        N/=2;
    }
    return binary;
}

