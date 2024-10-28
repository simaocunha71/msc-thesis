    transform(message.begin(), message.end(), message.begin(), ::toupper);
    string vowels = "AEIOU";
    for (int i=0;i<vowels.length();i++)
    {
        int pos = vowels.find(vowels[i]);
        message[pos+2] = message[pos+2] + 2;
    }
    return message;
}



