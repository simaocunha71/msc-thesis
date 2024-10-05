    int sum=0;
    char chr;
    for (int i=0;i<num.length();i++)
    {
        chr=num[i];
        if (chr>='A' && chr<='F')
        sum++;
    }
    return sum;
}

int main(){
    string num;
    int output;
    scanf("%s",&num);
    output=hex_key(num);
    printf("%d",output);
}


