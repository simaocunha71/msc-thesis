    int i;
    string output;
    for (i=0;i<s.length();i++)
    {
        int j;
        for (j=0;j<3;j++)
        {
            if (s.length()<=i+j) continue;
            if (s[i+j]=='0'+i%26)
            {
                output+=s[i+j];
                break;
            }
        }
    }
    return output;
}


