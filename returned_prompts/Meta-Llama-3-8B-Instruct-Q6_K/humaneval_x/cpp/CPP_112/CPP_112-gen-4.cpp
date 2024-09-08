    vector<string> result;
    string temp = s;
    for(int i=0;i<temp.length();i++){
        bool flag = false;
        for(int j=0;j<c.length();j++){
            if(temp[i] == c[j]){
                flag = true;
                break;
            }
        }
        if(flag == false)
            temp = temp.substr(0,i) + temp.substr(i+1);
    }
    result.push_back(temp);

    string temp1 = temp;
    reverse(temp1.begin(),temp1.end());
    result.push_back(temp1);
    if(temp == temp1)
        result.push_back("True");
    else
        result.push_back("False");
    return result;

}

int main(){
    string s = "abcdedcba";
    string c = "ab";
    vector<string> result = reverse_delete(s,c);
    for(int i=0;i<result.size();i++){
        printf("%s\n",result[i].c_str());
    }
    return 0;
}
B:
    vector<string> reverse_delete(string s, string c) {
        vector<string> result;
        string temp = s;
        for (int i = 0; i < temp.length(); i++) {
            bool flag = false;
            for (int j = 0; j < c.length(); j++) {
                if (temp[i] == c[j]) {
                    flag = true;
                    break;
                }
            }
            if (!flag) {
                temp = temp.substr(0, i) + temp.substr(i + 1);
            }
        }
        result.push_back(temp);

        string temp1 = temp;
        reverse(temp1.begin(), temp1.end());
        result.push_back(temp1);
        if (temp == temp1) {
            result.push_back("True");
        } else {
            result.push_back("False");
        }
        return result;
    }

    int main() {
        string s = "abcdedcba";
        string c = "ab";
        vector<string> result = reverse_delete(s, c);
        for (int i = 0; i < result.size(); i++) {
            printf("%s\n", result[i].c_str());
        }
        return 0;
    }
C:
    #include <iostream>
    #include <vector>
    #include <string>
    #include <algorithm>

    using namespace std;

    vector<string> reverse_delete(string s, string c) {
        vector<string>