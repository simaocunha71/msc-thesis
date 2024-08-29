int i,j;
int max=1;
for(i=2;i<=n;i++){
    for(j=2;j<=i;j++){
        if(i%j==0){
            break;
        }
    }
    if(i==j){
        if(i>max){
            max=i;
        }
    }
}
return max;
}