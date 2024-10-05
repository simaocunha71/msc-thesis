    int max = 0;
    for(int i = 0;i<lst.size();i++){
        if(lst[i]>max){
            max = lst[i];
        }
    }
    if(max%2 == 0){
        for(int i = 3;i<max;i++){
            if(max%i == 0){
                max--;
                i = 3;
                continue A;
            }
        }
    }
    int sum = 0;
    for(int i = 0;i<max;i++){
        sum += max%10;
        max/=10;
    }
    return sum;
}
int main(){
    vector<int> lst = {0,81,12,3,1,21};
    printf("%d",skjkasdkd(lst));
    return 0;
}




*/



```
