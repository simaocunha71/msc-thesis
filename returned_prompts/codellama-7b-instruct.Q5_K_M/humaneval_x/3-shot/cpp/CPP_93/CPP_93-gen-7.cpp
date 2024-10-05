    transform(message.begin(), message.end(), message.begin(), ::toupper);
    replace(message.begin(), message.end(), 'A', 'B');
    replace(message.begin(), message.end(), 'E', 'F');
    replace(message.begin(), message.end(), 'I', 'J');
    replace(message.begin(), message.end(), 'O', 'P');
    replace(message.begin(), message.end(), 'U', 'V');
    replace(message.begin(), message.end(), 'a', 'b');
    replace(message.begin(), message.end(), 'e', 'f');
    replace(message.begin(), message.end(), 'i', 'j');
    replace(message.begin(), message.end(), 'o', 'p');
    replace(message.begin(), message.end(), 'u', 'v');
    return message;
}


