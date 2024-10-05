    string result=s;
    int i,j;
    for (i=0;i<c.length();i++)
    {
        for (j=result.length()-1;j>=0;j--)
        {
            if (result[j]==c[i])
            {
                result=result.substr(0,j)+result.substr(j+1);
            }
        }
    }
    return vector<string>({result,is_palindrome(result)});
}

bool is_palindrome(string s){
    int i,j;
    int size=s.length();
    for (i=0;i<size/2;i++)
    {
        if (s[i]!=s[size-i-1])
        {
            return false;
        }
    }
    return true;
}


