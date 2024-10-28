    string new_message;
    int i;
    for (i=0;i<message.length();i++)
    {
        if (message[i]>='a' && message[i]<='z')
        {
            if (message[i]=='a' || message[i]=='e' || message[i]=='i' || message[i]=='o' || message[i]=='u')
            {
                new_message+=(message[i]-32+2);
            }
            else{
                new_message+=(message[i]+32);
            }
        }
        else if (message[i]>='A' && message[i]<='Z')
        {
            if (message[i]=='A' || message[i]=='E' || message[i]=='I' || message[i]=='O' || message[i]=='U')
            {
                new_message+=(message[i]+32+2);
            }
            else{
                new_message+=(message[i]-32);
            }
        }
        else{
            new_message+=message[i];
        }
    }

    return new_message;
}