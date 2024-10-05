    int a=0, b=1, count=0;
    while (count<n)
    {
        int temp=a+b;
        a=b;
        b=temp;
        if (is_prime(b))
        count+=1;
    }
    return b;
}

bool is_prime(int num)
{
    if (num <= 1) return 0;
    if (num == 2) return 1;
    if (num % 2 == 0) return 0;
    for (int i = 3; i * i <= num; i += 2) {
        if (num % i == 0)
            return 0;
    }
    return 1;
}
// Function to check if a number is prime


