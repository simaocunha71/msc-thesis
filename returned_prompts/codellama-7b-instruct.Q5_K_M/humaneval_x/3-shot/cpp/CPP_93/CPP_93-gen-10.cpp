    string encoded;
    int i;
    for (i=0;i<message.length();i++)
    {
        if (message[i]>='a'&&message[i]<='z')
        encoded+=message[i]-32;
        else if (message[i]>='A'&&message[i]<='Z')
        encoded+=message[i]+32;
        else
        encoded+=message[i];
    }
    return encoded;
}



