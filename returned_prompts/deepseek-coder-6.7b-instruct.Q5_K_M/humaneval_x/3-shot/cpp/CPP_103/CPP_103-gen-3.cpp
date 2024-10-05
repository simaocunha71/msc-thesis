    if(n>m)
    return "-1";
    int avg=(n+m)/2;
    int rounded_avg=floor(avg+0.5);
    string binary_avg="";
    while(rounded_avg){
        binary_avg=to_string(rounded_avg%2)+binary_avg;
        rounded_avg/=2;
    }
    return binary_avg;
}


