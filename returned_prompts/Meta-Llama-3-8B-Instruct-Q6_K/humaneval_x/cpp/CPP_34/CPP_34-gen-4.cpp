    vector<int> result;
    for(int i=0; i<l.size(); i++){
        if(find(result.begin(), result.end(), l[i]) == result.end()){
            result.push_back(l[i]);
        }
    }
    sort(result.begin(), result.end());
    return result;
}

int main() {
    vector<int> v = {5, 3, 5, 2, 3, 3, 9, 0, 123};
    vector<int> result = unique(v);
    for(int i=0; i<result.size(); i++){
        printf("%d ", result[i]);
    }
    printf("\n");
    return 0;
}
