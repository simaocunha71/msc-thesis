    int cnt = 0;
    for(int i = 0; i < s.size(); i+=2)
        if(isupper(s[i]))
            ++cnt;
    return cnt;
}

int main(void){
    string s;
    cin >> s;
    cout << count_upper(s) << endl;
    return 0;
}
