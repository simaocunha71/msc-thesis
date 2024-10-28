    string result;
    int i;
    int j;
    for (i=0;i<sentence.length();i++)
    if (sentence[i]==' ')
    {
        int len=0;
        for (j=i+1;j<sentence.length();j++)
        if (sentence[j]==' ')
        {
            len=j-i-1;
            break;
        }
        else
        len+=1;
        if (is_prime(len)==true)
        result=result+sentence.substr(i+1,len)+" ";
    }
    return result;
}

