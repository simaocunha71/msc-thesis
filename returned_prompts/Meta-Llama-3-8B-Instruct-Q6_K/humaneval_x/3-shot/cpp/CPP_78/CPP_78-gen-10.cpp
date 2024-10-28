    int count=0;
    for(int i=0; i<num.length();i++)
    {
        char c=num[i];
        if(c>='2' && c<='9')
        {
            if(c-'2'<=(c-'2')/2) count++;
        }
        else if(c>='A' && c<='F')
        {
            if(c-'A'<=(c-'A')/2) count++;
        }
    }
    return count;
}

// function to check whether a number is prime or not
bool isPrime(int n)
{
    if (n <= 1)
        return false;
    for (int i = 2; i <= sqrt(n); i++)
        if (n % i == 0)
            return false;
    return true;
}  // isPrime
// function to check whether a hexadecimal digit is prime
bool isHexPrime(char c)
{
    int n = c - '0';
    if (n >= 2 && n <= 9)
        return isPrime(n);
    else if (n >= 10 && n <= 13)
        return true;
    else
        return false;
}  // isHexPrime
// function to count the number of prime hexadecimal digits
int hex_key(string num)
{
    int count = 0;
    for (int i = 0; i < num.length(); i++)
    {
        char c = num[i];
        if (isHexPrime(c))
            count++;
    }
    return count;
}  // hex_key
