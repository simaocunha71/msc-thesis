    vector<int> v;
    for(int i = 0; i < l.size(); i++){
        bool found = false;
        for(int j = 0; j < v.size(); j++){
            if(l[i] == v[j]){
                found = true;
                break;
            }
        }
        if(!found){
            v.push_back(l[i]);
        }
    }
    sort(v.begin(), v.end());
    return v;
}

int main(){
    vector<int> l = {5, 3, 5, 2, 3, 3, 9, 0, 123};
    vector<int> result = unique(l);
    for(int i = 0; i < result.size(); i++){
        printf("%d ", result[i]);
    }
    printf("\n");
    return 0;
}
