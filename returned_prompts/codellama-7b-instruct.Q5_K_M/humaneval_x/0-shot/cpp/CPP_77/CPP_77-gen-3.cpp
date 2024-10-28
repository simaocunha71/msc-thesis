    if(a==0) return true;
    if(a<0) a=-a;
    int root=sqrt(a);
    if(root*root*root==a) return true;
    else return false;
}
int main(){
    int a=125;
    printf("%d",iscuber(a));
    return 0;
}
