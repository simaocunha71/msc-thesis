    map<char,int> m;
    char a;
    int b;
    for (int i = 0; i < test.size(); i++)
    {
        a = test[i];
        if (m.find(a) != m.end())
        {
            b = m[a];
            m[a] = b + 1;
        }
        else
        {
            m[a] = 1;
        }

    }
    return m;
}
int main()
{
    string s;
    while (cin>>s)
    {
        map<char,int> m;
        m = histogram(s);
        map<char,int>::iterator it;
        int max = 0;
        char c = ' ';
        for (it = m.begin(); it != m.end(); it++)
        {
            if (max < it->second)
            {
                max = it->second;
                c = it->first;
            }
        }
        cout<<c<<": "<<max<<endl;
    }
    return 0;
}


















































































































































































































































