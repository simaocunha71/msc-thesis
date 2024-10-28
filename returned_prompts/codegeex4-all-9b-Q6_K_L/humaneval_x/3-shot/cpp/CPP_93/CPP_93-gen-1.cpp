    int i;
    string new_message;
    for (i=0;i<message.length();i++)
    {
        char c=message[i];
        if (c>='a'&&c<='z')
        {
        if (c=='a')
        {
            new_message+='C';
        }
        else if (c=='e')
        {
            new_message+='G';
        }
        else if (c=='i')
        {
            new_message+='K';
        }
        else if (c=='o')
        {
            new_message+='Q';
        }
        else if (c=='u')
        {
            new_message+='W';
        }
        else if (c=='y')
        {
            new_message+='[';
        }
        else if (c=='A')
        {
            new_message+='C';
        }
        else if (c=='E')
        {
            new_message+='G';
        }
        else if (c=='I')
        {
            new_message+='K';
        }
        else if (c=='O')
        {
            new_message+='Q';
        }
        else if (c=='U')
        {
            new_message+='W';
        }
        else if (c=='Y')
        {
            new_message+='[';
        }
        else
        {
            new_message+=c+32;
        }
        }
        else
        {
            new_message+=c-32;
        }
    }
    return new_message;
}

