    vector<int> result;
    result.resize(numbers.size());
    int max = 0;
    for(int i = 0; i < numbers.size(); i++){
        if(numbers[i] > max){
            result[i] = numbers[i];
            max = numbers[i];
        }
        else{
            result[i] = max;
        }
    }
    return result;
}

int main(){
    vector<int> numbers = {1,2,3,2,3,4,2};
    for(int i : roll_max(numbers)){
        printf("%d ", i);
    }
    printf("\n");
}

/*
The problem is to generate a vector of rolling maximum element found until given moment in the sequence.

To solve the problem, we create a vector to store the result. For each element, if the current element is greater than the current maximum, we assign the current element to the result and update the maximum. Otherwise, we assign the maximum to the result.

Finally, we return the result vector.

The complexity of this solution is O(n), where n is the size of the input vector.

For the given input, the expected output is {1, 2, 3, 3, 3, 4, 4}.
*/










































































































































































































