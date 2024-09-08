    int max_prime = 0;
    for(int i = 0; i < lst.size(); i++){
        int num = lst[i];
        if(num > max_prime){
            max_prime = num;
        }
    }
    int sum = 0;
    while(max_prime > 0){
        sum += max_prime % 10;
        max_prime /= 10;
    }
    return sum;
}

int main(){
    vector<int> lst = {0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3};
    int output = skjkasdkd(lst);
    printf("Output: %d\n", output);
    return 0;
}
*/


