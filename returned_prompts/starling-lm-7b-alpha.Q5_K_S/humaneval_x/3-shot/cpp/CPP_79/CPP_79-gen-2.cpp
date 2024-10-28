    string binary="";
    while (decimal>0){
        binary="1"+binary;
        decimal=(decimal/2);
    }
    binary="db"+binary+"db";
    return binary;
}




