    vector<int> result(n);
    for(int i=1; i<=n; i++){
        if(i%2 == 0){
            int fact = 1;
            for(int j=1; j<=i; j++){
                fact *= j;
            }
            result[i-1] = fact;
        }
        else{
            int sum = 0;
            for(int j=1; j<=i; j++){
                sum += j;
            }
            result[i-1] = sum;
        }
    }
    return result;
}

int main(){
    int n = 5;
    vector<int> res = f(n);
    for(int i=0; i<n; i++){
        printf("%d ", res[i]);
    }
    return 0;
}

/*
