    int sum = 0;
    for(int i = 0; i < k; i++){
        if(arr[i] < 10){
            sum += arr[i];
        }
        else if(arr[i] < 100){
            sum += arr[i];
        }
        else{
            continue;
        }
    }
    return sum;
}

int main(){
    vector<int> arr = {111,21,3,4000,5,6,7,8,9};
    int k = 4;
    int sum = add_elements(arr,k);
    printf("The sum is : %d\n",sum);
    return 0;
}
