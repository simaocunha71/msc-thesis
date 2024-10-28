    int mid=(x+y)/2;
    if(x<=mid && mid<=y && mid%2==0) return mid;
    else if(mid%2==1) x=mid+1;
    else y=mid-1;
}

B:
int choose_num(int x,int y){
    for(int i=x;i<=y;i++){
        if(i%2==0) return i;
    }
    return -1;
}
