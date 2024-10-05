    vector<string> v;
    vector<string> words;
    int count=0;
    int start=0;
    for(int i=0;i<s.size();i++)
    {
        if(s[i]==' ')
        {
            if(count==n)
            {
                words.push_back(s.substr(start,i-start));
                v.push_back(s.substr(start,i-start));
                sort(v.begin(),v.end());
                start=i+1;
            }
            else if(count<n)
            {
                start=i+1;
            }
        }
        if(s[i]!=' ')
        {
            if(i==s.size()-1)
            {
                if(count==n)
                {
                    words.push_back(s.substr(start,i-start+1));
                    v.push_back(s.substr(start,i-start+1));
                    sort(v.begin(),v.end());
                }
            }
            else if(i!=s.size()-1)
            {
                if(s[i+1]==' ')
                {
                    if(count==n)
                    {
                        words.push_back(s.substr(start,i-start+1));
                        v.push_back(s.substr(start,i-start+1));
                        sort(v.begin(),v.end());
                    }
                }
            }
            count++;
        }
    }
    if(count==n)
    {
        v.push_back(s.substr(start,s.size()-start));
        sort(v.begin(),v.end());
    }
    return v;
}
int main()
{
    string s="Mary had a little lamb";
    int n=2;
    vector<string> v=select_words(s,n);
    for(int i=0;i<v.size();i++)
    {
        printf