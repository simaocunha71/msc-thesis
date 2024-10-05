    string res = "";
    for(auto s : strings){
        res += s;
    }
    return res;
}

vector<string> split(string s, char delimiter = ','){
    vector<string> res;
    while(s.find(delimiter) != string::npos){
        res.push_back(s.substr(0, s.find(delimiter)));
        s = s.substr(s.find(delimiter) + 1);
    }
    res.push_back(s);
    return res;
}

vector<string> read_strings(FILE *f){
    vector<string> res;
    for(string s; getline(f, s);){
        res.push_back(s);
    }
    return res;
}

string concatenate(vector<string> strings){
    string res = "";
    for(auto s : strings){
        res += s;
    }
    return res;
}

vector<string> read_strings(FILE *f){
    vector<string> res;
    for(string s; getline(f, s);){
        res.push_back(s);
    }
    return res;
}

vector<string> split(string s, char delimiter = ','){
    vector<string> res;
    while(s.find(delimiter) != string::npos){
        res.push_back(s.substr(0, s.find(delimiter)));
        s = s.substr(s.find(delimiter) + 1);
    }
    res.push_back(s);
    return res;
}

int main(void){
    FILE *f = fopen("test.txt", "r");
    vector<string> strings = read_strings(f);
    fclose(f);

    string concat = concatenate(strings);
    printf("%s\n", concat.c_str());
}











































