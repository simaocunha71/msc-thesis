    int count=0;
    int i;
    string str;
    for(i=0;i<nums.size();i++){
        if(nums[i]>10){
            str=to_string(abs(nums[i]));
            if((str[0]-'0')%2==1 && (str[str.length()-1]-'0')%2==1)
            count++;
        }
    }
    return count;
}

