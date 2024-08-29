int c=a;
int d=b;
int e=fabs(c);
int f=fabs(d);
int g=e%10;
int h=f%10;
int i=g*h;
return i;
}
int main(){
int a,b;
scanf("%d%d",&a,&b);
printf("%d\n",multiply(a,b));
return 0;
}
