    transform(message.begin(), message.end(), message.begin(), ::toupper);
    string vowels = "AEIOU";
    string vowels_2 = "BCDFGHJKLMNPQRSTVWXYZ";
    int i;
    for (i=0;i<vowels.size();i++)
    replace(message.begin(), message.end(), vowels[i], vowels_2[i]);
    return message;
}








