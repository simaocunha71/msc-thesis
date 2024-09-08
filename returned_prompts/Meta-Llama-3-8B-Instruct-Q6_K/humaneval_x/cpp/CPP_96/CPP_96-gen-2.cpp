    vector<int> result;
    if(n <= 1) return result;
    int i = 2;
    while(i < n){
        bool isPrime = true;
        for(int j = 2; j * j <= i; j++){
            if(i % j == 0){
                isPrime = false;
                break;
            }
        }
        if(isPrime){
            result.push_back(i);
        }
        i++;
    }
    return result;
}
int main(){
    printf("%lu", count_up_to(5).size());
    printf("\n");
    for(auto num: count_up_to(5)){
        printf("%d ", num);
    }
    printf("\n");
    return 0;
}
