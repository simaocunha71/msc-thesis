    int i, n = lst.size();
    long long sum = 0;
    for (i = 0; i < n; i++){
        if (lst[i] < 0 || lst[i] != round(lst[i])){
            continue;
        }
        if (lst[i] % 2){
            sum += pow(lst[i], 2);
        }
    }
    return sum;
}

int main(){
    vector<float> a = {1, 3, 2, 0};
    vector<float> b = {-1, -2, 0};
    vector<float> c = {9, -2};
    vector<float> d = {0};
    printf("%lld\n", double_the_difference(a));
    printf("%lld\n", double_the_difference(b));
    printf("%lld\n", double_the_difference(c));
    printf("%lld\n", double_the_difference(d));
    return 0;
}

