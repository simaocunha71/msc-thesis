    vector<string> result;
    for (auto& str : strings) {
        if (str.find(prefix) == 0) {
            result.push_back(str);
        }
    }
    return result;
}

B:
    vector<string> result;
    for (auto& str : strings) {
        if (str.start_with(prefix)) {
            result.push_back(str);
        }
    }
    return result;
}

C:
    vector<string> result;
    for (auto& str : strings) {
        if (str.startswith(prefix)) {
            result.push_back(str);
        }
    }
    return result;
}

D:
    vector<string> result;
    for (auto& str : strings) {
        if (str.startsWith(prefix)) {
            result.push_back(str);
        }
    }
    return result;
}

E:
    vector<string> result;
    for (auto& str : strings) {
        if (str.rfind(prefix) == 0) {
            result.push_back(str);
        }
    }
    return result;
}

F:
    vector<string> result;
    for (auto& str : strings) {
        if (str.startswith(prefix) && str.length() > prefix.length()) {
            result.push_back(str);
        }
    }
    return result;
}

G:
    vector<string> result;
    for (auto& str : strings) {
        if (str.find(prefix) != string::npos) {
            result.push_back(str);
        }
    }
    return result;
}

H:
    vector<string> result;
    for (auto& str : strings) {
        if (str.startswith(prefix)) {
            result.push_back(str);
        }
    }
    return result;
}

I:
    vector<string> result;
    for (auto& str : strings) {
        if (str.startswith(prefix)) {
            result.push_back(str);
        }
    }
    return result;
}

J:
    vector<string> result;
    for (auto& str : strings) {
        if (str.startswith(prefix)) {
            result.push_back(str);
        }
    }
    return result;
}

K:
    vector<string> result;
    for (auto& str : strings) {
        if (str.find(prefix) == 0) {
            result.push_back(str);
        }
    }
    return result;
}

L:
    vector<string> result;
    for (auto& str : strings) {
        if (str.startswith(prefix)) {
            result.push_back(str);
        }
    }
