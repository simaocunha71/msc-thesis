    int count = 0;
    for(int i = 0; i < num.length(); i++){
        char c = num[i];
        if(c >= '2' && c <= '7' || c == 'B' || c == 'D' || c == 'F')
            count++;
    }
    return count;
}

int main()
{
    string num = "ABED1A33";
    cout << "Count of hexadecimal digits that are primes: " << hex_key(num) << endl;
    return 0;
}

