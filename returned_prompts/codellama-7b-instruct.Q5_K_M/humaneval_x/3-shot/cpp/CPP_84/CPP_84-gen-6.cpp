    int binary[15],i,sum=0;
    string binary_string;
    for (i=0;i<15;i++)
    binary[i]=0;
    i=14;
    while (N>0){
        binary[i]=N%2;
        i--;
        N/=2;
    }
    for (i=0;i<15;i++)
    sum+=binary[i];
    binary_string=to_string(sum);
    return binary_string;
}






