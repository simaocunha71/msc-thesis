    long long sum = 0;
    for(int i = 0; i < lst.size(); i++){
        if(lst[i] > 0 && floor(lst[i]) == lst[i] && lst[i] % 2 == 1){
            sum += pow(lst[i], 2);
        }
    }
    return sum;
}

int main(){
    vector<float> lst = {1, 3, 2, 0};
    printf("%lld\n", double_the_difference(lst));  // Outputs: 10
    return 0;
}

The given code will output 10, which is the sum of squares of the odd numbers (1, 3) in the vector {1, 3, 2, 0}.


*/
int main(){
    vector<float> lst = {1, 3, 2, 0};
    printf("%lld\n", double_the_difference(lst));  // Outputs: 10
    return 0;
}
/*

