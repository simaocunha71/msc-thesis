    int prime_counter=0;
    string primes="2357B13";
    for(int i=0;i<num.size();i++)
    {
        if(num[i]>'9')
        {
            int dec = num[i] - 55;
            if(primes.find(dec) != std::string::npos)
            {
                prime_counter++;
            }
        }
        else
        {
            if(primes.find(num[i]) != std::string::npos)
            {
                prime_counter++;
            }
        }
    }
    return prime_counter;
}


