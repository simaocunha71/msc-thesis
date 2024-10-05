    if(n<=1)
        return y;
    else{
        for(int i=2;i<=n/2;i++){
            if(n%i==0)
                return x;
        }
        return y;
    }
}

int main(){
    int n;
    int x,y;
    scanf("%d",&n);
    scanf("%d",&x);
    scanf("%d",&y);
    printf("%d",x_or_y(n,x,y));
    return 0;
}


/*

Expected Output:

Input 1:
15 8 5
Output 1:
5

Input 2:
7 34 12
Output 2:
34

*/
