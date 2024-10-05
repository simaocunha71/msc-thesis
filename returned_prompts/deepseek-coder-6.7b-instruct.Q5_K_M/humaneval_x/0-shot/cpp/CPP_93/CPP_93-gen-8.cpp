for(int i=0; i<message.size(); i++){
    if(islower(message[i])){
        message[i] = toupper(message[i]);
    }
    else if(isupper(message[i])){
        message[i] = tolower(message[i]);
    }

    if(message[i] == 'a'){
        message[i]