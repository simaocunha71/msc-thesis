    int i=0;
    int sum=0;
    while(i<lst.size()){
        if(lst[i]%2==0){
            i++;
            continue;
        }
        sum+=lst[i];
        i++;
    }
    return sum;
}
int main(){
    vector<int> lst = {30,13,24,321};
    printf("sum is %d",solutions(lst));
    return 0;
}



