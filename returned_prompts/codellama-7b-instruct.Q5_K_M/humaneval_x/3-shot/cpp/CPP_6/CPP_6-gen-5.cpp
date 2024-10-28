    vector<int> result;
    string current;
    int level=0;
    int i;
    for (i=0;i<paren_string.length();i++)
    {
        if (paren_string[i]=='(')
        {
            level+=1;
            current+='(';
        }
        if (paren_string[i]==')')
        {
            level-=1;
            current+=')';
            if (level==0){
                result.push_back(current.length());
                current="";
            }
        }
    }
    return result;
}


