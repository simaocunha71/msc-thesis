vector<string> result;
for (string s : strings) {
    if (s.find(substring) != string::npos) {
        result.push_back(s);
    }
}
return result;
} // your code here

B:
vector<string> filter_by_substring(vector<string> strings, string substring) {
    return vector<string>(std::remove_if(strings.begin(), strings.end(),
        [&](const string& s) { return s.find(substring) == string::npos; }),
        strings.end());
}

C:
vector<string> filter_by_substring(vector<string> strings, string substring) {
    vector<string> result;
    for (string s : strings) {
        if (s.find(substring) != string::npos) {
            result.push_back(s);
        }
    }
    return result;
}

D:
vector<string> filter_by_substring(vector<string> strings, string substring) {
    return filter(lambda s: s.find(substring) != string::npos, strings);
}

E:
vector<string> filter_by_substring(vector<string> strings, string substring) {
    return filter(strings.begin(), strings.end(), 
        [&](const string& s) { return s.find(substring) == string::npos; });
}

F:
vector<string> filter_by_substring(vector<string> strings, string substring) {
    vector<string> result;
    for (string s : strings) {
        if (s.find(substring) != string::npos) {
            result.push_back(s);
        }
    }
    return result;
}

G:
vector<string> filter_by_substring(vector<string> strings, string substring) {
    vector<string> result;
    for (string s : strings) {
        if (s.find(substring) != string::npos) {
            result.push_back(s);
        }
    }
    return result;
}

H:
vector<string> filter_by_substring(vector<string> strings, string substring) {
    vector<string> result;
    for (string s : strings) {
        if (s.find(substring) != string::npos) {
            result.push_back(s);
        }
    }
    return result;
}

I:
vector<string> filter_by_substring(vector<string> strings, string substring) {
    vector<string> result;
    for (string s : strings) {
        if (s.find(substring) != string::npos) {
            result.push_back(s);
        }
    }
    return result;
}

J:
vector<string> filter_by_substring(vector<string> strings