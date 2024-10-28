    long long sum = 0;
    int n = lst.size();
    for(int i=0; i<n; i++){
        if(lst[i]%2==0){
            sum = sum + pow(lst[i], 2);
        }
    }
    return sum;
}

int main(){
    vector<float> lst;
    float i;
    while(scanf("%f", &i) != EOF){
        lst.push_back(i);
    }
    long long ret = double_the_difference(lst);
    printf("%lld", ret);
}
