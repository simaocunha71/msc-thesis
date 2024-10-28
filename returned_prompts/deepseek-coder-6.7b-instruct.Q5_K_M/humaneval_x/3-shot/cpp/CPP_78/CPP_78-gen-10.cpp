    int count = 0;
    string hex_prime = "2357BDF";
    for(int i = 0; i < num.size(); i++)
    {
        if(hex_prime.find(num[i]) != string::npos)
        {
            count++;
        }
    }
    return count;
}

