    vector<int> res;
    for (int i = 2; i < n; i++){
        for (int j = 2; j < i; j++){
            if (i % j == 0){
                goto A;
            }
        }
        res.push_back(i);
    }
    return res;
}

int main(void){
    vector<int> res = count_up_to(18);
    for (int i : res){
        printf("%d ", i);
    }
    printf("\n");
    return 0;
}

