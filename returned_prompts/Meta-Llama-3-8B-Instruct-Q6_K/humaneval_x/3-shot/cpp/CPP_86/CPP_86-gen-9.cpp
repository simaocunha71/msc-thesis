    string result;
    string word;
    int i;
    for (i=0;i<s.length();i++)
    {
        if (s[i]==' ')
        {
            result+=s[i];
        }
        else
        {
            word=s[i];
            for (int j=i+1;j<s.length();j++)
            {
                if (s[j]==' ')
                {
                    break;
                }
                word+=s[j];
            }
            for (char c:word)
            {
                result+=c;
            }
            for (char c:word)
            {
                result+=c;
            }
            i+=word.length()-1;
        }
    }
    return result;
}
/*
Output:
anti_shuffle("Hi") returns "Hi"
anti_shuffle("hello") returns "ehllo"
anti_shuffle("Hello World!!!") returns "Hello !!!Wdlor"
*/



