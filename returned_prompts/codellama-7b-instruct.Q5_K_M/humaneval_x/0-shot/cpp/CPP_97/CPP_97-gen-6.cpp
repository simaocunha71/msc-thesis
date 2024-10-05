  if(a<10&&b<10)
    return a*b;
  else{
    a=abs(a);
    b=abs(b);
    int temp=0,i=0,j=0,k=0;
    while(a!=0)
      temp+=a%10,a/=10;
    while(b!=0)
      temp+=b%10,b/=10;
    while(temp!=0)
      temp/=10,k++;
    temp=10;
    while(k--){
      while(temp!=0)
        temp/=10,i++;
      while(temp!=0)
        temp/=10,j++;
      temp=10;
    }
    temp=0;
    i--;
    j--;
    while(i>=0&&j>=0){
      temp+=a%10*b%10;
      a/=10;
      b/=10;
      i--;
      j--;
    }
    if(i<0){
      while(b!=0){
        temp+=a%10*b%10;
        a/=10;
        b/=10;
      }
    }
    else{
      while(a!=0){
        temp+=a%10*b%10;
        a/=10;
        b/=10;
      }
    }
    return temp;
  }
}
int main(){
  int a,b;
  scanf("%d %d",&a,&b);
  printf("%d",multiply(a,b));
  return 0;
}
