    int n = lst1.size();
    int m = lst2.size();
    bool found = false;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(lst1[i]%2 != 0 && lst2[j]%2 == 0){
                found = true;
                break;
            }
        }
        if(found) break;
    }
    if(found) return "YES";
    else return "NO";
}
B:
    int n = lst1.size();
    int m = lst2.size();
    for(int i = 0; i < n; i++){
        bool found = false;
        for(int j = 0; j < m; j++){
            if(lst1[i]%2 != 0 && lst2[j]%2 == 0){
                swap(lst1[i], lst2[j]);
                found = true;
                break;
            }
        }
        if(!found) return "NO";
    }
    return "YES";
}
C:
    int n = lst1.size();
    int m = lst2.size();
    for(int i = 0; i < n; i++){
        bool found = false;
        for(int j = 0; j < m; j++){
            if(lst1[i]%2 != 0 && lst2[j]%2 == 0){
                swap(lst1[i], lst2[j]);
                found = true;
                break;
            }
        }
        if(!found) return "NO";
    }
    return "YES";
}
D:
    sort(lst1.begin(), lst1.end());
    sort(lst2.begin(), lst2.end());
    for(int i = 0; i < lst1.size(); i++){
        if(lst1[i]%2 != 0) return "NO";
    }
    return "YES";
}
E:
    sort(lst1.begin(), lst1.end());
    sort(lst2.begin(), lst2.end());
    for(int i = 0; i < lst1.size(); i++){
        if(lst1[i]%2 != 0) return "NO";
    }
    return "YES";
}

F:
    sort(lst1.begin(), lst1.end());
    sort(lst2.begin(), lst2.end());
    for(int i = 0; i < lst1.size(); i++){
        if(lst1[i]%2 != 0) return "NO";
    }
    return "YES";
}
G:
