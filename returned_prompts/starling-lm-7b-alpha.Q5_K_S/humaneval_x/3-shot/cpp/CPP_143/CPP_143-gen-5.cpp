    string res;
    int i;
    for (i=0;i<sentence.length();i++)
    if (isalpha(sentence[i]))
    {
        int length=1;
        while (i+length<sentence.length() && isalpha(sentence[i+length]))
        length+=1;
        if (is_prime(length))
        res+=sentence.substr(i,length);
        i+=length-1;
    }
    return res;
}


