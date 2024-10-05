    if (num.find('A') != string::npos)
        return 1;
    else if (num.find('B') != string::npos)
        return 1;
    else if (num.find('C') != string::npos)
        return 1;
    else if (num.find('D') != string::npos)
        return 1;
    else if (num.find('E') != string::npos)
        return 1;
    else if (num.find('F') != string::npos)
        return 1;
    else
        return 0;
}
int hex_prime(string num){
    int i = 0;
    int n = 