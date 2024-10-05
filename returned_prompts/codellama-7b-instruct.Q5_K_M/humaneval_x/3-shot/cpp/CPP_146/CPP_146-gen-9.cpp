    int count=0;
    for (int i=0;i<nums.size();i++)
    {
        if (nums[i]>10){
            if (nums[i]%10>7 && nums[i]%10<3){
                count+=1;
            }
        }
    }
    return count;
}


