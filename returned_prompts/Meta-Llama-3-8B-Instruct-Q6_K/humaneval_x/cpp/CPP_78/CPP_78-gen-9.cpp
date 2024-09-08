    int count = 0;
    int len = num.length();
    for(int i = 0; i < len; i++)
    {
        if(num[i] == '2' || num[i] == '3' || num[i] == '5' || num[i] == '7' || num[i] == 'B' || num[i] == 'D')
        {
            count++;
        }
    }
    return count;
}
int main()
{
    string num = "ABED1A33";
    int result = hex_key(num);
    printf("The number of hexadecimal digits that are primes is %d.\n",result);
    return 0;
}

