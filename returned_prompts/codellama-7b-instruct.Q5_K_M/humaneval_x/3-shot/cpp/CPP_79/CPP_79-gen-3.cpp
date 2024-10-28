    string binary="db";
    while (decimal>0){
        binary+=decimal%2;
        decimal/=2;
    }
    binary+="db";
    return binary;
}


