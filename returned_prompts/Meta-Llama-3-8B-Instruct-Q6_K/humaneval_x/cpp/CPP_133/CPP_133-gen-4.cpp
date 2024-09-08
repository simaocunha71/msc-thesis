    int sum = 0;
    for(float x : lst){
        sum += ceil(x)*ceil(x);
    }
    return sum;
}
int main(){
    vector<float> lst = {1.4,4.2,0};
    printf("%d", sum_squares(lst));
    return 0;
}
