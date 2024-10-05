    string binary="";
    while(N>0){
        binary+=to_string(N%2);
        N/=2;
    }
    return binary;
}




