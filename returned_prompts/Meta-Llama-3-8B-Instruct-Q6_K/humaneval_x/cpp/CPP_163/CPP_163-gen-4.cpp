    vector<int> result;
    a=min(a,b);
    b=max(a,b);
    for(int i=a;i<=b;i++){
        int num=i;
        while(num>0){
            int digit=num%10;
            if(digit%2==0){
                result.push_back(digit);
            }
            num=num/10;
        }
    }
    return result;
}

int main(){
    int a,b;
    printf("Enter the range of even numbers\n");
    scanf("%d %d",&a,&b);
    vector<int> result=generate_integers(a,b);
    printf("Even digits between %d and %d are:\n",a,b);
    for(int i=0;i<result.size();i++){
        printf("%d ",result[i]);
    }
    printf("\n");
    return 0;
}
