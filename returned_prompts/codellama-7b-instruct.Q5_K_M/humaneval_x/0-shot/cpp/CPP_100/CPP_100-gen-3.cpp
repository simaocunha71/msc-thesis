    vector<int> result;
    for(int i = 0; i < n; i++){
        result.push_back(n);
        n = n % 2 == 0 ? n + 1 : n + 2;
    }
    return result;
}

int main(){
    vector<int> result = make_a_pile(3);
    for(int i : result){
        printf("%d ", i);
    }
    printf("\n");
    return 0;
}
