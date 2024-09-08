    int n = a.size();
    int m = b.size();
    int i = 0;
    int j = 0;
    string result = "";
    while(i < n && j < m){
        if(a[i] == '1' && b[j] == '1')
            result += '0';
        else if(a[i] == '0' && b[j] == '0')
            result += '0';
        else
            result += '1';
        i++;
        j++;
    }
    // remaining characters in a
    while(i < n){
        result += a[i];
        i++;
    }
    // remaining characters in b
    while(j < m){
        result += b[j];
        j++;
    }
    return result;
}
int main(){
    string a = "010";
    string b = "110";
    string res = string_xor(a,b);
    cout << res << endl;
    return 0;
}
