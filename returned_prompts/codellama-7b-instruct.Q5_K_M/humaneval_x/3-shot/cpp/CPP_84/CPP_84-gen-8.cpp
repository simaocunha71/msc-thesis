    string bin_string;
    int rem;
    int i;
    for (i=0;i<10000;i++)
    {
        rem=N%2;
        N=N/2;
        bin_string+=to_string(rem);
        if (N==0){
            return bin_string;
        }
    }
}



