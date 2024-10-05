    int i;
    string ans;
    for (i=0;i<text.length();i++)
    {
        if (text[i]==' ')
        {
            if (i>0 && text[i-1]==' ')
            {
                ans+="-";
                while (i<text.length() && text[i]==' ')
                i++;
            }
            else
            {
                ans+="_";
                while (i<text.length() && text[i]==' ')
                i++;
            }
        }
        else
        {
            ans+=text[i];
        }
    }
    return ans;
}


