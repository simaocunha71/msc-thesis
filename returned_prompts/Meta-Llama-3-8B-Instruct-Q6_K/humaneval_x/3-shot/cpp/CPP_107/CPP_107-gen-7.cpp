    vector<int> result;
    int even_count=0;
    int odd_count=0;
    for (int i=1;i<=n;i++)
    {
        string s=to_string(i);
        if (s==reverse(s))
        {
            if (i%2==0)
                even_count++;
            else
                odd_count++;
        }
    }
    result.push_back(even_count);
    result.push_back(odd_count);
    return result;
}  // reverse function not defined, implement it as well
string reverse(string str) {
    string rev;
    for(int i = str.length()-1; i >=0; i--)
        rev += str[i];
    return rev;
}  // define this function to reverse the string


