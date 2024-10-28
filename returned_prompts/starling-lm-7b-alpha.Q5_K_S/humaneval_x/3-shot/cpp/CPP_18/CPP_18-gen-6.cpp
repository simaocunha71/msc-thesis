    int result=0;
    int i=0,j=0;
    while (i<str.length())
    {
        while (j<substring.length())
        {
            if (str[i+j]!=substring[j])
            break;
            j+=1;
        }
        if (j==substring.length())
        {
            result+=1;
        }
        i+=1;
        j=0;
    }
    return result;
}



