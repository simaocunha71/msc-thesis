    if(strings.empty())
        return "";

B:
    string longest = strings[0];
    for(const string& s : strings){
        if(s.length() > longest.length())
            longest = s;
    }
    return longest;
}

int main() {
    vector<string> str = {"a", "bb", "ccc"};
    cout << longest(str) << endl;
    return 0;
}

/*
