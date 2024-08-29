    sort(l.begin(), l.end());
    vector<int> out;
    for (int i = 0; i < l.size(); i++){
        if (i == 0 || l[i] != l[i - 1]){
            out.push_back(l[i]);
        }
    }
    return out;
}

int main(){
    vector<int> l = {5, 3, 5, 2, 3, 3, 9, 0, 123};
    vector<int> out = unique(l);
    for (int i = 0; i < out.size(); i++){
        printf("%d ", out[i]);
    }
    printf("\n");
    return 0;
}
E:
1 2 3 5 9 123
