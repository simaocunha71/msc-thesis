    if(lst.size() < 2) return NULL;
    sort(lst.begin(), lst.end());
    for(int i=1; i<lst.size(); i++){
        if(lst[i] != lst[i-1]) return lst[i];
    }
    return NULL;
}

B:
    if(lst.empty()) return NULL;
    sort(lst.begin(), lst.end());
    if(lst.size() == 1) return NULL;
    return lst[1];
}

C:
    if(lst.size() < 2) return NULL;
    vector<int> lst2 = lst;
    sort(lst2.begin(), lst2.end());
    for(int i=0; i<lst2.size()-1; i++){
        if(lst2[i+1] != lst2[i]) return lst2[i+1];
    }
    return NULL;
}

D:
    if(lst.empty()) return NULL;
    int min = INT_MAX, second_min = INT_MAX;
    for(int i=0; i<lst.size(); i++){
        if(lst[i] < min) {
            second_min = min;
            min = lst[i];
        }
        else if(lst[i] < second_min && lst[i] != min)
            return lst[i];
    }
    return NULL;
}
int main(){
    printf("%d\n", next_smallest({1, 2, 3, 4, 5}));  // returns 2
    printf("%d\n", next_smallest({5, 1, 4, 3, 2}));  // returns 2
    printf("%d\n", next_smallest({}));  // returns None
    printf("%d\n", next_smallest({1, 1}));  // returns None
    return 0;
}

