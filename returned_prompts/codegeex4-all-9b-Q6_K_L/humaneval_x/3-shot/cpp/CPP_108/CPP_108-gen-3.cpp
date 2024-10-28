
For the first question, you have to check if the current pair of numbers is closer to each other than the threshold, and also check if the next pair of numbers is closer to each other than the threshold. If either of them is true, then return true. If neither is true, then return false.
Here is the corrected code:
bool has_close_elements(vector<float> numbers, float threshold){
    int i,j;

    for (i=0;i<numbers.size()-1;i++)
        for (j=i+1;j<numbers.size();j++)
            if (abs(numbers[i]-numbers[j])<threshold || abs(numbers[i+1]-numbers[j+1])<threshold)
                return true;

    return false;
}

For the fourth question, you have to check if the sum of digits of each number is greater than 0. If it is, then return 1. If it is not, then return 0.
Here is the corrected code:
int count_nums(vector<int> n){
    int i,j;
    int sum=0;
    for (i=0;i<n.size();i++)
    {
        sum=0;
        int num = abs(n[i]);
        while (num > 0)
        {
            sum += num % 10;
            num /= 10;
        }
        if (sum > 0)
            return 1;
    }
    return 0;
}