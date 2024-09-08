    vector<int> res;
    for(int i = 1; i <= n; i++){
        if(i % 2 == 0){
            int factorial = 1;
            for(int j = 1; j <= i; j++){
                factorial *= j;
            }
            res.push_back(factorial);
        }
        else{
            int sum = 0;
            for(int j = 1; j <= i; j++){
                sum += j;
            }
            res.push_back(sum);
        }
    }
    return res;

}

int main(){
    int n;
    printf("Enter the number of elements: ");
    scanf("%d", &n);
    vector<int> result = f(n);
    for(int i = 0; i < n; i++){
        printf("%d ", result[i]);
    }
    printf("\n");
    return 0;
}
