    vector<int> max_vector;
    int max = numbers[0];
    for(int i=0; i<numbers.size(); i++){
        if(numbers[i] > max){
            max = numbers[i];
        }
        max_vector.push_back(max);
    }
    return max_vector;
}

int main(){
    vector<int> nums = {1, 2, 3, 2, 3, 4, 2};
    vector<int> max_nums = rolling_max(nums);
    for(int i=0; i<max_nums.size(); i++){
        printf("%d ", max_nums[i]);
    }
    return 0;
}

*/

*/


int main() {
    vector<int> nums = {1, 2, 3, 2, 3, 4, 2};
    vector<int> max_nums = rolling_max(nums);
    for(int i=0; i<max_nums.size(); i++){
        printf("%d ", max_nums[i]);
    }
    return 0;
}

/*
