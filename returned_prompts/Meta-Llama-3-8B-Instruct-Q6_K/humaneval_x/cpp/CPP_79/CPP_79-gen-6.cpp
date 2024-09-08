    int n = decimal;
    string binary = "";
    while(n > 0){
        if(n % 2 == 0)
            binary = "0" + binary;
        else
            binary = "1" + binary;
        n = n / 2;
    }
    string result = "db" + binary + "db";
    return result;
}

int main(){
    printf("%s\n", decimal_to_binary(15).c_str());
    printf("%s\n", decimal_to_binary(32).c_str());
    return 0;
}

