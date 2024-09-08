    vector<int> res;
    if(n <= 1) return res;
    int i = 2;
    while(n > 1){
        if(n % i == 0){
            int count = 0;
            while(n % i == 0){
                n /= i;
                count++;
            }
            res.push_back(i);
            res.resize(res.size(), count);
        }
        i++;
    }
    return res;
}

int main(){
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    vector<int> result = factorize(n);
    printf("Prime factors: ");
    for(int i = 0; i < result.size(); i++){
        printf("%d ", result[i]);
    }
    printf("\n");
    return 0;
}
