    string binary="db";
    while(decimal!=0){
        binary=binary+((decimal%2==0)?"0":"1");
        decimal/=2;
    }
    binary+="db";
    return binary;
}


