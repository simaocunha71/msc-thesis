    int n = lst.size();
    int max = 0;
    int maxCnt = 0;
    for(int i = 0; i < n; i++){
        int cnt = 1;
        for(int j = i+1; j < n; j++){
            if(lst[i] == lst[j]){
                cnt++;
            }
        }
        if(cnt >= lst[i]){
            if(maxCnt < cnt){
                max = lst[i];
                maxCnt = cnt;
            }
        }
    }
    if(maxCnt < max){
        return -1;
    }
    return max;
}

int main(){
    vector<int> test1 = {4, 1, 2, 2, 3, 1};
    vector<int> test2 = {1, 2, 2, 3, 3, 3, 4, 4, 4};
    vector<int> test3 = {5, 5, 4, 4, 4};
    printf("%d\n", search(test1));
    printf("%d\n", search(test2));
    printf("%d\n", search(test3));
    return 0;
}


