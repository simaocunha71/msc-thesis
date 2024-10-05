    vector<int> v;
    for(int i = 1;i <= n;i++)
    {
        if(i % 2 == 0)
        {
            if((i / 10) % 10 == (i % 10))
            {
                v.push_back(1);
            }
            else
                v.push_back(0);
        }
        else
        {
            if((i / 10) % 10 + (i % 10) == 1)
            {
                v.push_back(1);
            }
            else
                v.push_back(0);
        }
    }
    return v;
}

int main()
{
    int n;
    scanf("%d", &n);
    vector<int> res = even_odd_palindrome(n);
    printf("%d,%d\n", res[0], res[1]);
    return 0;
}


*/











































































































































































































































































