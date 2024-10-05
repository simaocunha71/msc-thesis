    sort(arr.begin(),arr.end(),[&](int a,int b){
        int n1=a;
        int n2=b;
        int count1=0;
        int count2=0;
        while (n1>0)
        {
            count1+=n1%2;
            n1=n1/2;
        }
        while (n2>0)
        {
            count2+=n2%2;
            n2=n2/2;
        }
        if (count1==count2){
            return a<b;
        }
        return count1<count2;
    });
    return arr;
}

