    int len = a.length();
    int carry = 0;
    string res = "";
    for(int i = 0; i < len; i++){
        int x = a[i] - '0';
        int y = b[i] - '0';
        int temp = x ^ y ^ carry;
        carry = (x && y) || (x && carry) || (y && carry);
        res += temp + '0';
    }
    if(carry) res += '1';
    return res;
}

int main() {
    string a = "010";
    string b = "110";
    string result = string_xor(a, b);
    printf("%s\n", result.c_str());
    return 0;
}

