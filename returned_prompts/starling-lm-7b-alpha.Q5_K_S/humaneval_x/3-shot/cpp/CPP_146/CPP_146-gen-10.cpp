    int i,c=0,x,y;
    for (i=0;i<nums.size();i++)
    {
        x=nums[i];
        y=abs(x);
        if (y>10 && (x%10)%2==1 && (x/10)%10%2==1)
        c+=1;
    }
    return c;
}


