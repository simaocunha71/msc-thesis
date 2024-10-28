    string binary_number;
    int i,remainder;
    int temp_N=N;
    while (temp_N>0)
    {
        remainder=temp_N%2;
        binary_number+=(char)(remainder+'0');
        temp_N/=2;
    }
    return binary_number;
}


