    vector<int> res;
    while(n != 1){
        if(n % 2 == 0){
            n /= 2;
        }
        else{
            n = n * 3 + 1;
        }
        if(n % 2 != 0){
            res.push_back(n);
        }
    }
    sort(res.begin(), res.end());
    return res;
}

int main(){
    int n;
    printf("Enter a positive integer: ");
    scanf("%d", &n);
    vector<int> res = get_odd_collatz(n);
    printf("The odd numbers in the Collatz sequence are: ");
    for(int i = 0; i < res.size(); i++){
        printf("%d ", res[i]);
    }
    printf("\n");
    return 0;
}

