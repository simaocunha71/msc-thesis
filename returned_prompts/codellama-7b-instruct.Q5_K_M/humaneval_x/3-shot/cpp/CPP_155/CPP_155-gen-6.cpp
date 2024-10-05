    string s=to_string(num);
    vector<int> even_odd;
    for (int i=0;i<s.length();i++)
    if (s[i]%2==0)
    even_odd[0]+=1;
    else
    even_odd[1]+=1;
    return even_odd;
}




