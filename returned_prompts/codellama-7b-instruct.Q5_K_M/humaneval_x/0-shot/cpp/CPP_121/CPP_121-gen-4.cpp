    int sum=0;
    for(int i=0;i<lst.size();i+=2){
        if(lst[i]%2!=0)
            sum+=lst[i];
    }
    return sum;
}
int main(){
    int a[]={5, 8, 7, 1};
    vector<int> lst(a,a+sizeof(a)/sizeof(a[0]));
    printf("%d",solutions(lst));
    return 0;
}


