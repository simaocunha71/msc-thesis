    int count = 0;
    for (int i = 0; i < nums.size(); i++)
    {
        if (nums[i] > 10)
        {
            int firstDigit = abs(nums[i]/10);
            int lastDigit = abs(nums[i]%10);
            if (firstDigit%2==1 && lastDigit%2==1)
            {
                count++;
            }
        }
    }
    return count;
}


