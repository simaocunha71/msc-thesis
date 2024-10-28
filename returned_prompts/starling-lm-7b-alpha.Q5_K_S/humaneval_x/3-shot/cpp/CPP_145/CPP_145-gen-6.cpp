    vector<int> nums1;
    vector<int> nums2;
    vector<int> result;
    int i;
    int sum;
    int length;
    int index;
    for (i=0;i<nums.size();i++)
    {
        sum=0;
        length=nums[i];
        while (length!=0){
            sum+=length%10;
            length/=10;
        }
        index=nums.size()-i-1;
        if (sum<0)sum=-sum;
        if (sum<=0)nums1.push_back(nums[i]);
        if (sum>0)nums2.push_back(sum);
    }
    sort(nums1.begin(), nums1.end());
    sort(nums2.begin(), nums2.end());
    for (i=0;i<nums1.size();i++)
    {
        result.push_back(nums1[i]);
        if (i<nums2.size())result.push_back(nums2[i]);
    }
    return result;
}








































































































































































































































