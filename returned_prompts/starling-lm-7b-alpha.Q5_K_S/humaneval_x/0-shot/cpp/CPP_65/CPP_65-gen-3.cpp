    int a[1000];
    int k=0;
    while(x>0){
        a[k++]=x%10;
        x/=10;
    }
    if(shift>=k){
        for(int i=k-1;i>=0;i--)
            a[i+shift]=a[i];
        for(int i=0;i<k;i++)
            a[i+k-shift]=a[i];
        string res="";
        for(int i=0;i<k;i++)
            res+=string(1,a[i]+'0');
        return res;
    }else{
        for(int i=0;i<k;i++)
            a[i+shift]=a[i];
        for(int i=k-1;i>=shift;i--)
            a[i+k-shift]=a[i];
        string res="";
        for(int i=0;i<k;i++)
            res+=string(1,a[i]+'0');
        return res;
    }
}

int main(){
    int x,shift;
    scanf("%d%d",&x,&shift);
    string res=circular_shift(x,shift);
    printf("%s\n",res.c_str());
    return 0;
}


























































































































































































