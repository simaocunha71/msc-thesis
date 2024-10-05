return (int) (1<<n)%p;
}
int main(){
int n,p;
scanf("%d %d",&n,&p);
printf("%d",modp(n,p));
return 0;
}

