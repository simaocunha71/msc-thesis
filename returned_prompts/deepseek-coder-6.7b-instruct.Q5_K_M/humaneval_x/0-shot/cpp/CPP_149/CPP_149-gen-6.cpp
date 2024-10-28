sort(lst.begin(), lst.end(), [](const std::string &a, const std::string &b){
    if(a.size() % 2 != 0 && b.size() % 2 != 0) return a < b;
    return a.size() < b.size();
});

B:
vector<string> ret;
for(const string &s: lst){
    if(s.size() % 2 == 0) ret.push_back(s);
}
return ret;
}

C:
vector<string> ret;
for(const string &s: lst){
    if(s.size() % 2 == 0) ret.push_back(s);
}
return ret;
}

D:
for(auto it = lst.begin(); it != lst.end(); ++it){
    if(it->size() % 2 != 0) lst.erase(it);
}

E:
vector<string> ret;
for(const string &s: lst){
    if(s.size() % 2 == 0) ret.push_back(s);
}
return ret;
}

F:
vector<string> ret;
for(const string &s: lst){
    if(s.size() % 2 == 0) ret.push_back(s);
}
return ret;
}

G:
vector<string> ret;
for(const string &s: lst){
    if(s.size() % 2 == 0) ret.push_back(s);
}
return ret;
}

H:
for(auto it = lst.begin(); it != lst.end(); ++it){
    if(it->size() % 2 != 0) lst.erase(it);
}

I:
vector<string> ret;
for(const string &s: lst){
    if(s.size() % 2 == 0) ret.push_back(s);
}
return ret;
}

J:
vector<string> ret;
for(const string &s: lst){
