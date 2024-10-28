if(n>m) return "-1";
int sum=0;
for(int i=n;i<=m;i++) sum=sum+i;
sum=sum/2;
return to_string(sum);
}

