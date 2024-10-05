    int number=stoi(value);
    int dec=stoi(value.substr(value.find('.')+1));
    if (dec>5)
    return number+1;
    if (dec<5)
    return number;
    if (dec==5)
    return number+int(number%2);
    return 0;
}

