    vector<string> result;
    for(const auto& s : strings){
        if(s.find(prefix) == 0)
            result.push_back(s);
    }
    return result;
}

B:
    vector<string> result;
    for(const auto& s : strings){
        if(s.substr(0, prefix.size()) == prefix)
            result.push_back(s);
    }
    return result;
}

C:
    vector<string> result;
    for(const auto& s : strings){
        if(s.rfind(prefix) == 0)
            result.push_back(s);
    }
    return result;
}

D:
    vector<string> result;
    for(const auto& s : strings){
        if(s.find(prefix) != string::npos)
            result.push_back(s);
    }
    return result;
}

E:
    vector<string> result;
    for(const auto& s : strings){
        if(s.startsWith(prefix))
            result.push_back(s);
    }
    return result;
}

F:
    vector<string> result;
    for(const auto& s : strings){
        if(s.startswith(prefix))
            result.push_back(s);
    }
    return result;
}
G:
    vector<string> result;
    for(const auto& s : strings){
        if(s.find(prefix) != string::npos)
            result.push_back(s);
    }
    return result;
}

H:
    vector<string> result;
    for(const auto& s : strings){
        if(s.startswith(prefix))
            result.push_back(s);
    }
    return result;
}

I:
    vector<string> result;
    for(const auto& s : strings){
        if(s.find(prefix) == 0)
            result.push_back(s);
    }
    return result;
}

J:
    vector<string> result;
    for(const auto& s : strings){
        if(s.rfind(prefix) == string::npos)
            result.push_back(s);
    }
    return result;
}

K:
    vector<string> result;
    for(const auto& s : strings){
        if(s.rfind(prefix) == 0)
            result.push_back(s);
    }
    return result;
}

L:
    vector<string> result;
    for(const auto& s : strings){
        if(s.find(prefix) != 0)
            result.push_back(s);
    }
    return result;
}

M:
    vector<string> result;
    for(const auto& s : strings){
        if(s.rfind(prefix) != 0)
            result.push_back(s);
    }
   