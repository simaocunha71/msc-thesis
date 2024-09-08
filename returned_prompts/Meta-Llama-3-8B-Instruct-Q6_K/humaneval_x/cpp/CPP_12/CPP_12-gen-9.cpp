    if(strings.empty()) return ""; // Return empty string if input is empty
    string longest_str = strings[0]; // Initialize longest string as the first string in the vector
    for(int i = 1; i < strings.size(); i++){
        if(strings[i].size() > longest_str.size()) longest_str = strings[i]; // Update longest string if a longer one is found
    }
    return longest_str;
} 

B:
    if(strings.empty()) return ""; // Return empty string if input is empty
    string longest_str = *max_element(strings.begin(), strings.end(), [](string a, string b)->bool{return a.size() < b.size();});
    return longest_str;
} 

C:
    if(strings.empty()) return ""; // Return empty string if input is empty
    string longest_str = *max_element(strings.begin(), strings.end(), [](string a, string b)->bool{return a.size() < b.size();});
    return longest_str;
} 

D:
    if(strings.empty()) return ""; // Return empty string if input is empty
    string longest_str = *max_element(strings.begin(), strings.end(), [](string a, string b)->bool{return a.size() < b.size();});
    return longest_str;
} 

E:
    if(strings.empty()) return ""; // Return empty string if input is empty
    string longest_str = *max_element(strings.begin(), strings.end(), [](string a, string b)->bool{return a.size() < b.size();});
    return longest_str;
} 

F:
    if(strings.empty()) return ""; // Return empty string if input is empty
    string longest_str = *max_element(strings.begin(), strings.end(), [](string a, string b)->bool{return a.size() < b.size();});
    return longest_str;
} 

G:
    if(strings.empty()) return ""; // Return empty string if input is empty
    string longest_str = *max_element(strings.begin(), strings.end(), [](string a, string b)->bool{return a.size() < b.size();});
    return longest_str;
} 

H:
    if(strings.empty()) return ""; // Return empty string if input is empty
    string longest_str = *max_element(strings.begin(), strings.end(), [](string a, string b)->bool{return a.size() < b.size();});
    return longest_str;
} 

I:
    if(strings.empty()) return ""; // Return empty string if input is empty
    string longest_str = *max_element(strings.begin(), strings