    for (int i=0;i<message.length();i++)
    {
        if (message[i]>='A' && message[i]<='z')
        {
            if (message[i]>='a')
            message[i]+=2;
            else
            message[i]-=2;
        }
        if (message[i]>='A' && message[i]<='Z')
        {
            if (message[i]>='a')
            message[i]+=2;
            else
            message[i]-=2;
        }
    }
    return message;
}


