    int count=0;
    int temp;
    for(int i=0;i<n.size();i++){
        temp=abs(n[i]);
        while(temp>0){
            if(n[i]<0 && i==0) count+=temp%10;
            else count+=temp%10;
            temp=temp/10;
        }
    }
    return count;
}


