    string prime_hex = "2357BDF";
    int count = 0;
    for(char & c: num)
    {
        if(prime_hex.find(c)!=string::npos) count++;
    }
    return count;
}



