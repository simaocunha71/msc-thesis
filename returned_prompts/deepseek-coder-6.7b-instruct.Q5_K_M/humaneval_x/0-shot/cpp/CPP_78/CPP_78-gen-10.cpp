    int counter = 0;
    string prime_hex = "2357BDF";
    transform(num.begin(), num.end(), num.begin(), ::toupper);
    for(int i=0; i<num.size(); i++){
        if(prime_hex.find(num[i]) != string::npos)
            counter++;
    }
    return counter;
}

int main(){
    printf("%d\n",hex_key("AB"));
    printf("%d\n",hex_key("1077E"));
    printf("%d\n",hex_key("ABED1A33"));
    printf("%d\n",hex_key("123456789ABCDEF0"));
    printf("%d\n",hex_key("2020"));
}

