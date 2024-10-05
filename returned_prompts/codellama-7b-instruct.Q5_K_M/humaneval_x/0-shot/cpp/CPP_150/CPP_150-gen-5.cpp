    if (n==3){
        return x;
    }
    else{
        return y;
    }
}

int main(){
    int n,x,y;
    scanf("%d %d %d",&n,&x,&y);
    int ans=x_or_y(n,x,y);
    printf("%d",ans);
    return 0;
}
