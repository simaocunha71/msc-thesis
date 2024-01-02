/*
From a given vector of integers, generate a vector of rolling maximum element found until given moment
in the sequence.
>>> rolling_max({1, 2, 3, 2, 3, 4, 2})
{1, 2, 3, 3, 3, 4, 4}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> rolling_max(vector<int> numbers){
	int index = 0;
	int max = -1; //Maximum element found so far
	if (numbers[index] <= 0) {
        return max;
    } else if(numbers[index+1] > numbers[index]){
      index++; //move to next position since last was smaller than present one
    }
	while(index < numbers.size()){
      if(numbers[index] >= 0) {
        max = numbers[index];
        index++;
      } else {
        break;
      }
	}
return max;
}
int main(){
	rolling_max({1,2,3,2,3,4,2});
	return 0;
}
