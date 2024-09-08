    string binary;
    while(decimal > 0){
        binary.push_back((decimal % 2) + '0');
        decimal /= 2;
    }
    reverse(binary.begin(), binary.end());
    string result = "db" + binary + "db";
    return result;
}
int main(){
    int decimal;
    cout << "Enter the decimal number: ";
    cin >> decimal;
    cout << "The binary equivalent is: " << decimal_to_binary(decimal) << endl;
    return 0;
}

