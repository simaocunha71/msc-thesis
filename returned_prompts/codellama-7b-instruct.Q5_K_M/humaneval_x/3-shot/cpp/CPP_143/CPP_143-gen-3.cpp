    string new_sentence;
    int i;
    for (i=0;i<sentence.length();i++)
    {
        if (is_prime(sentence[i]))
        new_sentence+=sentence[i];
    }
    return new_sentence;
}

bool is_prime(char ch){
    int i;
    for (i=2;i<ch;i++)
    if (ch%i==0)
    return false;
    return true;
}


