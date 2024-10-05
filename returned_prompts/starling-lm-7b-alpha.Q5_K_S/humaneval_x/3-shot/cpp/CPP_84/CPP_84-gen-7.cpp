    string binary="";
    int i,j,remainder;
    for (i=N;i>0;i=i/2)
    {
        remainder=i%2;
        binary+=to_string(remainder);
    }
    return binary;
}


