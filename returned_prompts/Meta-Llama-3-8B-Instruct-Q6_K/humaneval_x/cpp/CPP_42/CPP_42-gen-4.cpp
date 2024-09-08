    vector<int> result = l;
    for(int i = 0; i < result.size(); i++){
        result[i]++;
    }
    return result;
}

B:
    vector<int> result;
    for(int i = 0; i < l.size(); i++){
        result.push_back(l[i] + 1);
    }
    return result;
}

C:
    vector<int> result;
    for(int i = 0; i < l.size(); i++){
        result[i] = l[i] + 1;
    }
    return result;
}

D:
    vector<int> result;
    for(int i = 0; i < l.size(); i++){
        result.push_back(l[i]);
        result[i] = result[i] + 1;
    }
    return result;
}

E:
    vector<int> result;
    for(int i = 0; i < l.size(); i++){
        result.push_back(l[i] + 1);
    }
    return result;
}

F:
    vector<int> result;
    for(int i = 0; i < l.size(); i++){
        result[i] = l[i] + 1;
    }
    return result;
}

G:
    vector<int> result = l;
    for(int i = 0; i < l.size(); i++){
        result[i]++;
    }
    return result;
}

H:
    vector<int> result;
    for(int i = 0; i < l.size(); i++){
        result.push_back(l[i]);
        result[i] = result[i] + 1;
    }
    return result;
}

I:
    vector<int> result;
    for(int i = 0; i < l.size(); i++){
        result[i] = l[i] + 1;
    }
    return result;
}

J:
    vector<int> result;
    for(int i = 0; i < l.size(); i++){
        result.push_back(l[i]);
    }
    for(int i = 0; i < result.size(); i++){
        result[i]++;
    }
    return result;
}

K:
    vector<int> result;
    for(int i = 0; i < l.size(); i++){
        result.push_back(l[i]);
    }
    return result;
}

L:
    vector<int> result;
    for(int i = 0; i < l.size(); i++){
        result[i] = l[i] + 1;
    }
    return result;
