    vector<string> res;
    string result = "";
    for(int i = 0; i < s.size(); i++){
        bool flag = false;
        for(int j = 0; j < c.size(); j++){
            if(s[i] == c[j]){
                flag = true;
                break;
            }
        }
        if(!flag){
            result += s[i];
        }
    }
    res.push_back(result);
    bool is_palindrome = true;
    for(int i = 0; i < result.size(); i++){
        if(result[i] != result[result.size() - i - 1]){
            is_palindrome = false;
            break;
        }
    }
    res.push_back(is_palindrome ? "True" : "False");
    return res;
}
int main()
{
    string s = "abcdedcba";
    string c = "ab";
    vector<string> res = reverse_delete(s,c);
    for(auto i : res)
        printf("%s\n",i.c_str());
    return 0;
}

B:
    #include<string>
    #include<vector>
    #include<algorithm>
    using namespace std;

    vector<string> reverse_delete(string s, string c) {
        vector<string> res;
        string result = "";
        for (int i = 0; i < s.size(); i++) {
            bool flag = false;
            for (int j = 0; j < c.size(); j++) {
                if (s[i] == c[j]) {
                    flag = true;
                    break;
                }
            }
            if (!flag) {
                result += s[i];
            }
        }
        res.push_back(result);

        bool is_palindrome = true;
        string temp = result;
        reverse(temp.begin(), temp.end());
        if (temp != result) {
            is_palindrome = false;
        }
        res.push_back(is_palindrome ? "True" : "False");
        return res;
    }

    int main() {
        string s = "abcdedcba";
        string c = "ab";
        vector<string> res = reverse_delete(s, c);
        for (auto i : res)
            cout << i << endl;
        return 0;
    }C:
    #include<string>
    #include<vector>
    #include<algorithm>
    using namespace std;

    vector<string> reverse_delete(string s, string c) {
        vector<string> res;
        string result = "";
        for (int