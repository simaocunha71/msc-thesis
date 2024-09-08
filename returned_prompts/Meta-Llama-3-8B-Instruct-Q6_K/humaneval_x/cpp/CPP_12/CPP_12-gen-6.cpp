    if(strings.empty())
        return "";
    string longest_str = strings[0];
    for(int i = 1; i < strings.size(); i++){
        if(strings[i].length() > longest_str.length()){
            longest_str = strings[i];
        }
    }
    return longest_str;
}

B:
    if(strings.empty())
        return "";
    string longest_str = *max_element(strings.begin(), strings.end(),
        [](const string& a, const string& b)->bool{return a.length() < b.length();});
    return longest_str;
}

C:
    if(strings.empty())
        return "";
    string longest_str = *max_element(strings.begin(), strings.end(),
        [](const string& a, const string& b)->bool{return a.length() < b.length();});
    return longest_str;
}

D:
    if(strings.empty())
        return "";
    return *max_element(strings.begin(), strings.end(), [](const string& a, const string& b)->bool{return a.length() < b.length();});

}
E:
    if(strings.empty())
        return "";
    return *max_element(strings.begin(), strings.end(), [](const string& a, const string& b)->bool{return a.length() < b.length();});

}
F:
    if(strings.empty())
        return "";
    return *max_element(strings.begin(), strings.end(),
        [](const string& a, const string& b)->bool{return a.length() < b.length();});

}

G:
    if(strings.empty())
        return "";
    return *max_element(strings.begin(), strings.end(), [](const string& a, const string& b)->bool{return a.length() < b.length();});

}
H:
    if(strings.empty())
        return "";
    return *max_length(strings.begin(), strings.end(),
        [](const string& a, const string& b)->bool{return a.length() < b.length();});

}
I:
    if(strings.empty())
        return "";
    return *max_element(strings.begin(), strings.end(),
        [](const string& a, const string& b)->bool{return a.length() < b.length();});

}
J:
    if(strings.empty())
        return "";
    return *max_element(strings.begin(), strings.end(),
        [](const string& a, const string& b)->bool{return a.length() < b.length();});

}
K:
    if(strings.empty())
        return "";
    return *max_element(strings.begin(), strings.end(),
        [](const string& a, const string& b)->bool{return a.length() < b.length();