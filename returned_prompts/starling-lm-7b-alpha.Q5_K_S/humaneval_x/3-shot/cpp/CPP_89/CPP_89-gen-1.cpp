    string result;
    int i;
    for (i=0;i<s.length();i++)
    {
        if (s[i]==' '){result+=' ';}
        else if (s[i]>='a' && s[i]<='z'){result+=char( (int(s[i])-97+2*2)%26 +97 );}
        else if (s[i]>='A' && s[i]<='Z'){result+=char( (int(s[i])-65+2*2)%26 +65 );}
    }
    return result;
}



