    int i,key=0;
    for (i=0;i<num.length();i++)
    {
        char chr=num[i];
        if (chr>='0'&&chr<='9')
        {
            key+=(chr-'0');
        }
        if (chr>='A'&&chr<='F')
        {
            key+=10;
            chr=chr-'A'+10;
            key+=chr;
        }
    }
    return key;
}

int is_prime(int num){

    int i;
    if (num==2||num==3||num==5||num==7)
    return 1;
    if (num%2==0||num%3==0||num%5==0||num%7==0)
    return 0;
    for (i=2;i<sqrt(num);i++)
    if (num%i==0)
    return 0;
    return 1;
}

int count_hex_prime(string num){

    int i,key,count=0;
    key=hex_key(num);
    for (i=0;i<key;i++)
    if (is_prime(i))
    count++;
    return count;
}


