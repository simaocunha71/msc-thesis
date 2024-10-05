    int sum=0;
    string binary;
    while (N>0)
    {
        if (N%2==0)
            binary='0'+binary;
        else
            binary='1'+binary;
        N=N/2;
        sum++;
    }
    for (int i=sum-1;i>=0;i--)
        if (binary[i]=='1')
            return binary;
    return "0";
} // end of solve function
// The function solve is called with an argument: solve(1000)


