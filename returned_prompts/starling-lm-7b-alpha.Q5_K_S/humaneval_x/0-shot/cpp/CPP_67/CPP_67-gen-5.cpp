    int len = s.size();
    int a = 0;
    int b = 0;
    int i;
    for(i = 0;i < len;i++)
    {
        if(s[i] >= '0' && s[i] <= '9')
        {
            a = a * 10 + s[i] - '0';
        }
        else
        {
            if(s[i] == 'a')
            {
                b++;
            }
            else
            {
                i++;
                b = b * 10 + s[i] - '0';
            }
        }
    }
    return n - a - b;
}
int main()
{
    string s = "2 apples and 3 oranges";
    int n = 100;
    printf("%d\n",fruit_distribution(s,n));
    return 0;
}

*/
























































































































































































































































































