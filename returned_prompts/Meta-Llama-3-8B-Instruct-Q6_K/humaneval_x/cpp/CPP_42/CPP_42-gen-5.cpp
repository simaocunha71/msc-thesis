    vector<int> res;
    for(auto x : l){
        res.push_back(x+1);
    }
    return res;
}

int main(){
    vector<int> v={1, 2, 3};
    vector<int> result = incr_list(v);
    for(auto x : result){
        printf("%d ",x);
    }
    printf("\n");
    return 0;
}
