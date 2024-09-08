    vector<string> result;
    int i = 0;
    while(i<s.size()){
        while(i<s.size() && s[i] == ' '){
            i++;
        }
        int j = i;
        while(j<s.size() && s[j] != ',' && s[j] != ' '){
            j++;
        }
        result.push_back(s.substr(i,j-i));
        i = j;
    }
    return result;
}

int main(){
    string s = "Hi, my name is John";
    vector<string> v = words_string(s);
    for(int i = 0; i < v.size(); i++){
        printf("%s\n", v[i].c_str());
    }
    return 0;
}

Output:
Hi
my
name
is
John

