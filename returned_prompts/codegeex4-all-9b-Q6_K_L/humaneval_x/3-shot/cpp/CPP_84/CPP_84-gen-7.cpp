    string binary="";
    int number=N;
    while (number>0){
        if (number%2==0)
            binary+='0';
        else
            binary+='1';
        number=number/2;
    }
    string reverse_binary="";
    for (int i=binary.length()-1;i>=0;i--)
        reverse_binary+=binary[i];
    return reverse_binary;
}

