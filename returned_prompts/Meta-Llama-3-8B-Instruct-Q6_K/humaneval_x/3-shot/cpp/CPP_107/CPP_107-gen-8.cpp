    vector<int> result(2,0);
    for(int i = 1; i <= n; i++) {
        string str = to_string(i);
        if(str == reverse(str).str()) {
            if(i % 2 == 0) result[0]++;
            else result[1]++;
        }
    }
    return result;
}
string reverse(string str) {
    string reversed = "";
    for(int i = str.length()-1; i >= 0; i--) {
        reversed += str[i];
    }
    return reversed;
} // Function to reverse the string.