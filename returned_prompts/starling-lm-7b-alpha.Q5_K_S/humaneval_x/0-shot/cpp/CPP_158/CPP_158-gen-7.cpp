    string ans = " ";
    int max = 0;
    for(int i=0; i<words.size(); i++) {
        int count = 0;
        int len = words[i].length();
        bool vis[len];
        for(int j=0; j<len; j++)
            vis[j] = false;
        for(int j=0; j<len; j++) {
            if(vis[j]) continue;
            count++;
            for(int k=j; k<len; k++) {
                if(words[i][j] == words[i][k])
                    vis[k] = true;
            }
        }
        if(count > max) {
            max = count;
            ans = words[i];
        } else if(count == max && words[i] < ans) {
            ans = words[i];
        }
    }
    return ans;
}
int main() {
    vector<string> words;
    while(true) {
        string s;
        cin >> s;
        if(cin.eof()) break;
        words.push_back(s);
    }
    cout << find_max(words) << endl;
    return 0;
}

*/
















































































































































































































