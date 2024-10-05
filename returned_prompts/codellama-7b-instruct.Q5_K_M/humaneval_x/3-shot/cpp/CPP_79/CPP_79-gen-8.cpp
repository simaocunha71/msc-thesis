    string binary;
    binary="db";
    while (decimal>0){
        binary=binary+(decimal%2)+"";
        decimal=decimal/2;
    }
    binary=binary+"db";
    return binary;
}



