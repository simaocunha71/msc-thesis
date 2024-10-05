    transform(message.begin(), message.end(), message.begin(), ::toupper);
    transform(message.begin(), message.end(), message.begin(), [](char c){
        if (isalpha(c)){
            if (c=='A' || c=='a')
            return 'X';
            if (c=='E' || c=='e')
            return 'D';
            if (c=='I' || c=='i')
            return 'B';
            if (c=='O' || c=='o')
            return 'P';
            if (c=='U' || c=='u')
            return 'Y';
        }
        return c;
    });
    return message;
}


