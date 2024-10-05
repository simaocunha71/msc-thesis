    if (n>m) return "-1";
    float avg=n+(m-n)/2;
    int rounded_avg=avg;
    string binary;
    while (rounded_avg!=0)
    {
        binary+=rounded_avg%2;
        rounded_avg/=2;
    }
    return binary;
}






