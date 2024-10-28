    string binary="db";
    int i=0;
    while (decimal>0){
        binary+=decimal%2;
        decimal/=2;
    }
    return binary+"db";
}


