    if(s.length() < 3)
        return false;
    for(int i = 0; i < s.length() - 2; i++)
    {
        set<char> st;
        for(int j = i; j < i+3; j++)
        {
            st.insert(s[j]);
        }
        if(st.size() < 3)
            return false;
    }
    return true;
}
int main()
{
    string s;
    cin>>s;
    if(is_happy(s))
        cout<<"True\n";
    else
        cout<<"False\n";
    return 0;
}
