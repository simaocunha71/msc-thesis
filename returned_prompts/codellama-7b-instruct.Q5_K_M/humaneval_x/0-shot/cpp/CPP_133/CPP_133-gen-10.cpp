    int n = lst.size();
    int sum = 0;
    for(int i = 0; i < n; i++){
        sum += pow(ceil(lst[i]), 2);
    }
    return sum;
}
int main(){
    vector<float> lst = {-2.4, 1, 1};
    printf("sum is %d", sum_squares(lst));
    return 0;
}
