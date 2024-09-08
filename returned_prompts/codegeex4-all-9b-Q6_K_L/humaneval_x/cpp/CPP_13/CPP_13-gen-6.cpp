int i,j;
int count=0;
for(i=1;i<=a;i++){
    if(a%i==0){
        count++;
    }
}
for(j=1;j<=b;j++){
    if(b%j==0){
        count++;
    }
}
return count;

B:
int i,j;
int count=0;
for(i=1;i<=a;i++){
    if(a%i==0){
        count++;
    }
}
for(j=1;j<=b;j++){
    if(b%j==0){
        count++;
    }
}
return count/2;
