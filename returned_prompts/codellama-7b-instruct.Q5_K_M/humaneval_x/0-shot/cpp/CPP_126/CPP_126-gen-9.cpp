    for(int i=0; i<lst.size()-1; i++){
        if(lst[i] > lst[i+1]){
            return false;
        }
    }
    return true;
}
int main(){
    vector<int> lst = {1, 2, 2, 2, 3, 4};
    bool res = is_sorted(lst);
    printf("%d", res);
    return 0;
}

A: 
    for(int i=0; i<lst.size()-1; i++){
        if(lst[i] > lst[i+1]){
            return false;
        }
    }
    return true;
}

bool is_sorted(vector<int> lst){

    sort(lst.begin(), lst.end());
    for(int i=0; i<lst.size()-1; i++){
        if(lst[i] == lst[i+1]){
            return false;
        }
    }
    return true;
}

bool is_sorted(vector<int> lst){
    sort(lst.begin(), lst.end());
    for(int i=0; i<lst.size()-1; i++){
        if(lst[i] == lst[i+1]){
            return false;
        }
    }
    return true;
}

bool is_sorted(vector<int> lst){
    sort(lst.begin(), lst.end());
    for(int i=0; i<lst.size()-1; i++){
        if(lst[i] == lst[i+1]){
            return false;
        }
    }
    return true;
}

bool is_sorted(vector<int> lst){
    sort(lst.begin(), lst.end());
    for(int i=0; i<lst.size()-1; i++){
        if(lst[i] == lst[i+1]){
            return false;
        }
    }
    return true;
}

bool is_sorted(vector<int> lst){
    sort(lst.begin(), lst.end());
