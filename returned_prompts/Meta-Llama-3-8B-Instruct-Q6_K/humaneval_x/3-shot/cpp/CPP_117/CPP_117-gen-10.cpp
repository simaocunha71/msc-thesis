    vector<string> result;
    int i, j;
    for (i=0;i<s.length();i++)
    {
        if (s[i]==' ')
        {
            string word=s.substr(j,i-j);
            int count=0;
            for (j=i+1;j<s.length();j++)
            {
                if (s[j]==' ')
                {
                    i=j;
                    break;
                }
                else
                {
                    if ((s[j]-'a'<='z'&&s[j]-'a'>='a')||(s[j]-'A'<='Z'&&s[j]-'A'>='A'))
                        count++;
                }
            }
            word=s.substr(j,i-j);
            if (count==n)
                result.push_back(word);
        }
    }
    sort(result.begin(),result.end());
    return result;
}


