    string binary="";
    int i=0;
    while (decimal>0){
        binary+=to_string(decimal%2);
        decimal=decimal/2;
    }
    binary="db"+binary+"db";
    return binary;
}

