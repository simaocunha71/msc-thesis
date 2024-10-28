    string bin="",bin1="";
    int i,j,dec=decimal,rem,div;
    for(i=0;dec>0;i++)
    {
        rem=dec%2;
        bin1=to_string(rem)+bin1;
        dec/=2;
    }
    bin="db"+bin1+"db";
    return bin;
}




/*
You will be given a string of binary numbers and a number. Your task is to check if the string of
binary numbers is equal to the binary representation of the given number. In other words, you should
convert the given number to binary and compare it to the string of binary numbers. If both are the same,
return true; otherwise, return false.

Examples:
is_equal(decimal_to_binary(15),"db1111db") // returns true
is_equal(decimal_to_binary(32),"db100000db") // returns true
is_equal(decimal_to_binary(32),"db100001db") // returns false
*/
bool is_equal(string binary,string bin){
    bool b=true;
    int i,j,n1=binary.length(),n2=bin.length();
    if(n1!=n2)
        b=false;
    else
    {
        for(i=0;i<n1;i++)
        {
            if(binary[i]!=bin[i])
                b=false;
        }
    }
    return b;
}




/*
You will be given a string of binary numbers. Your task is to count the number of '0's in the string.

Examples:
count_zeros("db100000db") // returns 4
count_zeros("db1111111db") // returns 0
count_zeros("db00010000db") // returns 3
*/
int count_zeros(string bin){
    int i,j,n=bin.length(),c=0;
    for(i=2;i<