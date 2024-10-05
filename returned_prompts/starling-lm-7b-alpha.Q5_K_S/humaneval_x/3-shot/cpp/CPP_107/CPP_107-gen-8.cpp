    vector<int> even_odd;
    int i;
    int j;
    int even_count=0;
    int odd_count=0;
    for (i=1;i<=n;i++)
    {
        if (i%2==0)
        {
        string number=to_string(i);
        j=number.length();
        bool palindrome=true;
        for (int k=0;k<j/2;k++)
        {
        if (number[k]!=number[j-k-1])
        {
        palindrome=false;
        break;
        }
        }
        if (palindrome)
        {
        even_count+=1;
        }
        }
        else
        {
        string number=to_string(i);
        j=number.length();
        bool palindrome=true;
        for (int k=0;k<j/2;k++)
        {
        if (number[k]!=number[j-k-1])
        {
        palindrome=false;
        break;
        }
        }
        if (palindrome)
        {
        odd_count+=1;
        }
        }
    }
    even_odd.push_back(even_count);
    even_odd.push_back(odd_count);
    return even_odd;
}


