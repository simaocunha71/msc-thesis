    for (int i=0;i<message.length();i++){
        if (message[i]>='a' && message[i]<='z'){
            if (message[i]=='a')
            message[i]='K';
            if (message[i]=='e')
            message[i]='I';
            if (message[i]=='i')
            message[i]='o';
            if (message[i]=='o')
            message[i]='i';
            if (message[i]=='u')
            message[i]='A';
        }
        if (message[i]>='A' && message[i]<='Z'){
            if (message[i]=='A')
            message[i]='k';
            if (message[i]=='E')
            message[i]='i';
            if (message[i]=='I')
            message[i]='O';
            if (message[i]=='O')
            message[i]='I';
            if (message[i]=='U')
            message[i]='a';
        }
    }
    return message;
}


