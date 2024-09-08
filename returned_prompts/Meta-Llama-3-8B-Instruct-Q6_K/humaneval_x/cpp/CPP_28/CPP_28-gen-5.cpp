    string result = "";
    for(auto str : strings){
        result += str;
    }
    return result;
}

B:
    string result = "";
    for(string str : strings){
        result += str;
    }
    return result;
}

C:
    string result = "";
    for(string str : strings){
        result += str + " ";
    }
    return result.substr(0, result.size() - 1);
}

D:
    string result = "";
    for(auto str : strings){
        result += str + " ";
    }
    return result.substr(0, result.size() - 1);
}

E:
    string result = "";
    for(string str : strings){
        result += str + " ";
    }
    return result;
}

F:
    return *strings.begin();
}

G:
    return *strings.end();
}

H:
    return strings[0];
}

I:
    return strings[strings.size() - 1];
}

J:
    return strings[0] + strings[strings.size() - 1];
}

K:
    return strings[0] + strings[strings.size() - 1];
}

L:
    return strings[0] + strings[strings.size() - 1];
}

M:
    return strings[0] + strings[strings.size() - 1];
}

N:
    return strings[0] + strings[strings.size() - 1];
}

O:
    return strings[0] + strings[strings.size() - 1];
}

P:
    return strings[0] + strings[strings.size() - 1];
}

