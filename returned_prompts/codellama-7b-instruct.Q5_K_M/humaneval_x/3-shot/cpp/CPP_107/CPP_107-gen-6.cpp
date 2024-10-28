    int even_count=0,odd_count=0;
    for (int i=1;i<n;i++)
    {
        if (is_palindrome(i)&&i%2==0)
        even_count++;
        if (is_palindrome(i)&&i%2!=0)
        odd_count++;
    }
    return {even_count,odd_count};
}


bool is_palindrome(int num)
{
    int rev=0;
    int temp=num;
    while (temp)
    {
        int rem=temp%10;
        rev=rev*10+rem;
        temp=temp/10;
    }
    if (rev==num)
    return true;
    else
    return false;
}


