    int even_pal=0, odd_pal=0;
    for (int i=1;i<=n;i++)
    {
        string s=to_string(i);
        bool is_palindrome=true;
        for (int j=0;j<s.length()/2;j++)
        {
            if (s[j]!=s[s.length()-1-j])
            {
                is_palindrome=false;
                break;
            }
        }
        if (is_palindrome && i%2==0) even_pal++;
        if (is_palindrome && i%2!=0) odd_pal++;
    }
    return {even_pal, odd_pal};
}
