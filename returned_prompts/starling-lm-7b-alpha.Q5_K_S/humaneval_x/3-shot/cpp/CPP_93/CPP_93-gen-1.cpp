    int i;
    char chr;
    for (i=0;i<message.length();i++)
    {
        chr=message[i];
        if (chr>='a' && chr<='z'){
        message[i]=char(chr-'a'+'z'-'a'+1+'a');
        }
        else if (chr>='A' && chr<='Z'){
        message[i]=char(chr-'A'+'Z'-'A'+1+'A');
        }
    }
    for (i=0;i<message.length();i++)
    {
        chr=message[i];
        if (chr=='a'){
        message[i]='c';
        }
        if (chr=='e'){
        message[i]='g';
        }
        if (chr=='i'){
        message[i]='k';
        }
        if (chr=='o'){
        message[i]='q';
        }
        if (chr=='u'){
        message[i]='w';
        }
    }
    return message;
}


