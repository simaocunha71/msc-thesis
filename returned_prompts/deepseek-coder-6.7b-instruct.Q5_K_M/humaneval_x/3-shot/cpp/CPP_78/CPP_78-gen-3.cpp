    int count=0;
    string prime_hex = "2357BDF";
    for(char c: num)
        if(prime_hex.find(c)!=string::npos)
            count++;
    return count;
}


