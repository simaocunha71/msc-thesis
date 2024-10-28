    vector<int> even_digits;
    if (a>b)
    {
        int temp;
        temp=a;
        a=b;
        b=temp;
    }
    for (int i=a;i<=b;i++)
    {
        int digit;
        while (i!=0)
        {
            digit=i%10;
            if (digit%2==0)
            {
                even_digits.push_back(digit);
            }
            i=i/10;
        }
    }
    return even_digits;
}

