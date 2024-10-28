    vector<int> prime;
    int sum=0;
    int max=0;
    for(int i=0;i<lst.size();i++){
        for(int j=2;j<lst[i];j++){
            if(lst[i]%j==0){
                break;
            }
            if(j==lst[i]-1){
                prime.push_back(lst[i]);
                if(lst[i]>max){
                    max=lst[i];
                }
            }
        }
    }
    while(max>0){
        sum+=max%10;
        max/=10;
    }
    return sum;
}
int main(){
    vector<int> lst = {0,81,12,3,1,21};
    printf("%d\n", skjkasdkd(lst));
    return 0;
}

*/

//Q2:
/*
