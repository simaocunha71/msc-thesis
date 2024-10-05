    int count=0;
    for(int i=0;i<n.size();i++){
        int temp=n[i];
        int sign=temp<0?-1:1;
        temp=temp<0?-temp:temp;
        while(temp){
            int digit=temp%10;
            temp/=10;
            if(digit*sign>0)
                count++;
        }
    }
    return count;
}
//test
int main(){
    vector<int> nums={-1,-11,1,11,2};
    int result=count_nums(nums);
    printf("%d",result);
}
/*
Write a function which takes a vector of integers and returns the number of
elements which has a sum of digits > 0. If a number is negative, then its first
signed digit will be negative: e.g. -123 has signed digits -1, 2, and 3.
>>> count_nums({}) == 0
>>> count_nums({-1, 11, -11}) == 1
>>> count_nums({1, 1, 2}) == 3
*/
