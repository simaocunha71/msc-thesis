    string bin_number="";
    int i,digit,sum=0;
    for (i=0;i<5;i++)
    {
        digit=N%2;
        bin_number+=to_string(digit);
        sum+=digit;
        N=N/2;
    }
    return to_string(sum);
}


