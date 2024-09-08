    int count=0;
    for(int i=0; i<n.size(); i++){
        int num = n[i];
        int sign = 1;
        if(num < 0){
            sign = -1;
            num = -num;
        }
        int sum = 0;
        while(num > 0){
            int digit = num % 10;
            sum += digit;
            num /= 10;
        }
        if(sum > 0){
            count++;
        }
    }
    return count;
}

int main(){
    vector<int> v = {-1, 11, -11};
    printf("%d", count_nums(v));
    return 0;
}
