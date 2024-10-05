    int count = 0;
    for(int i = 0; i < s.length(); i += 2){
        if(s[i] >= 'a' && s[i] <= 'z'){
            count++;
        }
    }
    return count;
}

int main(){
    string s;
    cin >> s;
    cout << count_lower(s