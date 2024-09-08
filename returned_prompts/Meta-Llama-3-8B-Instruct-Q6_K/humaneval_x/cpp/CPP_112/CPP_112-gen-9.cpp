    vector<string> result;
    string str;
    for(int i=0;i<s.length();i++)
    {
        bool flag = false;
        for(int j=0;j<c.length();j++)
        {
            if(s[i] == c[j])
            {
                flag = true;
                break;
            }
        }
        if(!flag)
        {
            str += s[i];
        }
    }
    result.push_back(str);
    string rev = str;
    reverse(rev.begin(),rev.end());
    if(rev == str)
    {
        result.push_back("True");
    }
    else
    {
        result.push_back("False");
    }
    return result;
}
int main()
{
    string s,c;
    cin>>s>>c;
    vector<string> ans = reverse_delete(s,c);
    for(int i=0;i<ans.size();i++)
    {
        cout<<ans[i]<<" ";
    }
    return 0;
}
B:
    #include<stdio.h>
    #include<vector>
    #include<string>
    #include<algorithm>
    using namespace std;
    vector<string> delete_and_check_palindrome(string s, string c) {
        vector<string> result;
        string str;
        for (int i = 0; i < s.length(); i++) {
            bool flag = false;
            for (int j = 0; j < c.length(); j++) {
                if (s[i] == c[j]) {
                    flag = true;
                    break;
                }
            }
            if (!flag) {
                str += s[i];
            }
        }
        result.push_back(str);
        string rev = str;
        reverse(rev.begin(), rev.end());
        if (rev == str) {
            result.push_back("True");
        } else {
            result.push_back("False");
        }
        return result;
    }
    int main() {
        string s, c;
        cin >> s >> c;
        vector<string> ans = delete_and_check_palindrome(s, c);
        for (int i = 0; i < ans.size(); i++) {
            cout << ans[i] << " ";
        }
        return 0;
    }
C:
    #include<stdio.h>
    #include<vector>
    #include<string>
    #include<algorithm>
    using namespace std;
    vector<string> delete_and_check_palindrome(string s, string c) {
        vector<string> result;
        string str;
        for (