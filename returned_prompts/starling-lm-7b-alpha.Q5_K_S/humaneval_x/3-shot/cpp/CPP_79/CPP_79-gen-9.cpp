    string binary="";
    int level=0;
    int i;
    while (decimal>0){
        binary+='1'+'0'+'1'+'0' + (decimal%2+'0');
        decimal/=2;
    }
    return "db"+binary+"db";
}


