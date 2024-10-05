    if(arr.empty()) return -32768;
    int sign_product = 1;
    int magnitude_sum = 0;
    for(int i = 0; i<arr.size(); i++){
        if(arr[i] != 0){
            if(arr[i] < 0) sign_product = -sign_product;
            magnitude_sum += abs(arr[i]);
        }
    }
    return sign_product * magnitude_sum;
}
int main(){
    vector<int> v = {-1, 2, 2, -4};
    printf("%d\n", prod_signs(v));
    return 0;
}
