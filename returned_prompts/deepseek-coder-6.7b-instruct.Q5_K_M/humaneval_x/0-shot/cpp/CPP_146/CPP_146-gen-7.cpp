    int count = 0;
    for(int i=0; i<nums.size(); i++){
        if(nums[i] > 10){
            int lastDigit = abs(nums[i] % 10);
            int firstDigit = abs((nums[i] / pow(10, (int)log10(abs(nums[i])))) % 10);
            if(lastDigit % 2 != 0 && firstDigit % 2 != 0){
                count++;
            }
        }
    }
    return count;
}

*/

#include <vector>
#include <cmath>

int specialFilter(std::vector<int> nums) {
    int count = 0;
    for (int num : nums) {
        if (num > 10) {
            int lastDigit = abs(num % 10);
            int firstDigit = abs((num / pow(10, (int)log10(abs(num)))) % 10);
            if (lastDigit % 2 != 0 && firstDigit % 2 != 0) {
                count++;
            }
        }
    }
    return count;
}

/*
