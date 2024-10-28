int fizz_buzz(int n)
{
    int ans = 0, i;
    for (i = 11; i < n; i += 11, i++)
    {
        if (i % 13 == 0)
        {
            if (i % 7 == 0)
            {
                ans++;
            }
        }
    }
    return ans;
}