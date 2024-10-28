    int count=0;
    for (int i=0;i<num.length();i++)
    {
        char c=num[i];
        if (c>='2' && c<='9')
        {
            if (c-'2'==1 || c-'2'==3 || c-'2'==5 || c-'2'==7)
                count++;
        }
        else if (c>='A' && c<='F')
        {
            if (c-'A'+10==11 || c-'A'+10==13)
                count++;
        }
    }
    return count;
}
int main()
{
    string num="1077E";
    int result = hex_key(num);
    printf("Number of primes: %d\n",result);
    return 0;
}
