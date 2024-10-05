    int i,n=paren_string.size();
    vector<string> res;
    string s="";
    for(i=0;i<n;i++)
    {
        if(paren_string[i]=='(')
        {
            s.clear();
            s+='(';
        }
        else if(paren_string[i]==')')
        {
            if(s.size()>0 && s[s.size()-1]=='(') res.push_back(s);
            s.clear();
        }
        else s+=paren_string[i];
    }
    if(s.size()>0 && s[s.size()-1]=='(') res.push_back(s);
    return res;
}

int main()
{
    string paren_string="( ) (( )) (( )( ))";
    vector<string> res;
    res = separate_paren_groups(paren_string);
    for(int i=0;i<res.size();i++) printf("%s\n",res[i].c_str());
    return 0;
}















































































































































































































































