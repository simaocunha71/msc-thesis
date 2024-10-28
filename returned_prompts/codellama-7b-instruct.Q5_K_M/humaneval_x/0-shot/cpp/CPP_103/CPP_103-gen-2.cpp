int sum=0;
int count=0;
if(n>m){
    return "-1";
}
for(int i=n;i<=m;i++){
    sum+=i;
    count++;
}
double average=sum/count;
int result=round(average);
string str;
str=to_string(result);
return str;
