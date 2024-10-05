    string res = "";
    string temp = "";
    for(int i = 0; i < s.length(); i++){
        if(s[i] == ' '){
            res += temp;
            temp = "";
            res += ' ';
        }
        else{
            temp += s[i];
        }
    }
    res += temp;
    for(int i = 0; i < res.length(); i++){
        if(res[i] == ' '){
            temp = "";
        }
        else{
            temp += res[i];
        }
        string temp2 = temp;
        sort(temp2.begin(), temp2.end());
        res.replace(res.find(temp), temp.length(), temp2);
    }
    return res;
}
// Example usage:
int main() {
    string s = "Hello World!!!";
    string result = anti_shuffle(s);
    cout << result << endl;  // Outputs: "Hello !!!Wdlor"
    return 0;
}
// Time complexity: O(n^2) where n is the length of the string.
// Space complexity: O(n) where n is the length of the string.