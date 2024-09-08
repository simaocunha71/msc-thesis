vector<string> result;
for(const string& str : lst){
    if(str.length() % 2 == 0){
        result.push_back(str);
    }
}
sort(result.begin(), result.end(), [](const string& a, const string& b){
    if(a.length() == b.length()){
        return a < b;
    }
    return a.length() < b.length();
});
return result;
}

B:
vector<string> sorted_list_sum(vector<string> lst){
    vector<string> result;
    for(const string& str : lst){
        if(str.length() % 2 == 0){
            result.push_back(str);
        }
    }
    sort(result.begin(), result.end());
    return result;
}

C:
vector<string> sorted_list_sum(vector<string> lst){
    vector<string> result;
    for(const string& str : lst){
        if(str.length() % 2 == 0){
            result.push_back(str);
        }
    }
    sort(result.begin(), result.end(), [](const string& a, const string& b){
        if(a.length() == b.length()){
            return a < b;
        }
        return a.length() < b.length();
    });
    return result;
}

D:
vector<string> sorted_list_sum(vector<string> lst){
    vector<string> result;
    for(const string& str : lst){
        if(str.length() % 2 == 0){
            result.push_back(str);
        }
    }
    sort(result.begin(), result.end(), [](const string& a, const string& b){
        return to_string(a.length()).compare(to_string(b.length()));
    });
    return result;
}

E:
vector<string> sorted_list_sum(vector<string> lst){
    vector<string> result;
    for(const string& str : lst){
        if(str.length() % 2 == 0){
            result.push_back(str);
        }
    }
    sort(result.begin(), result.end(), [](const string& a, const string& b){
        int lena = a.length();
        int lenb = b.length();
        if(lena == lenb){
            return a < b;
        }
        return lena < lenb;
    });
    return result;
}

F:
vector<string> sorted_list_sum(vector<string> lst){
    vector<string> result;
    for(const string& str : lst){
        if(str.length() % 2 == 0){
            result.push_back(str);
        }
    }
    sort(result.begin(), result.end(), [](