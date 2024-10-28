    vector<int> max_nums;
    int max_num = numbers[0];
    for(int i=0; i<numbers.size(); i++){
        if(numbers[i] > max_num){
            max_num = numbers[i];
        }
        max_nums.push_back(max_num);
    }
    return max_nums;
}
int main(){
    vector<int> numbers = {1, 2, 3, 2, 3, 4, 2};
    vector<int> max_nums = rolling_max(numbers);
    for(int i=0; i<max_nums.size(); i++){
        printf("%d ", max_nums[i]);
    }
    return 0;
}

//Explanation
The function rolling_max iterates over the input vector of integers and for each position, if the current element is greater than the current maximum, it updates the maximum. Then it appends the current maximum to the output vector. The function returns the output vector.

In the main function, we call rolling_max with the given vector of integers and print the elements of the resulting vector.

This program will output:
1 2 3 3 3 4 4
*/

#include<stdio.h>
#include<vector>
using namespace std;
vector<int> rolling_max(vector<int> numbers){
    vector<int> max_nums;
    int max_num = numbers[0];
    for(int i=0; i<numbers.size(); i++){
        if(numbers[i] > max_num){
            max_num = numbers[i];
        }
        max_nums.push_back(max_num);
    }
    return max_nums;
}
int main(){
    vector<int> numbers = {1, 2, 3, 2, 3, 4, 2};
    vector<int> max_nums = rolling_max(numbers);
    for(int i=0; i<max_nums.size(); i++){
        printf("%d ", max