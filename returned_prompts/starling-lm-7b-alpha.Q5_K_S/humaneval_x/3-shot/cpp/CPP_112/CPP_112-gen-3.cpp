    string result=s;
    int i,j;
    for (i=0;i<result.length();i++)
    {
        for (j=0;j<c.length();j++)
        {
            if (result[i]==c[j])
            {
                result.erase(i,1);
                break;
            }
        }
    }
    return {result,is_palindrome(result)};
}

string is_palindrome(string s){
    int i,j;
    for (i=0,j=s.length()-1;i<j;i++,j--)
    {
        if (s[i]!=s[j])
        return "False";
    }
    return "True";
}


