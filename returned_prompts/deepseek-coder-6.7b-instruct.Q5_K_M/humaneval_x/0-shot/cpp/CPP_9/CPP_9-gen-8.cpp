    vector<int> result;
    int max = numbers[0];
    result.push_back(max);
    for(int i=1; i<numbers.size(); i++){
        if(numbers[i] > max){
            max = numbers[i];
        }
        result.push_back(max);
    }
    return result;
}
int main() {
    vector<int> numbers = {1, 2, 3, 2, 3, 4, 2};
    vector<int> max_elements = rolling_max(numbers);
    for(int i=0; i<max_elements.size(); i++){
        printf("%d ", max_elements[i]);
    }
    return 0;
}
*/

/*
O:
The output of the given program will be:
1 2 3 3 3 4 4

This output is the sequence of maximum elements found in the original sequence until each moment.
*/

/*
R:
The rolling_max function works by iterating over the input vector of integers. For each integer, it checks if it is greater than the current maximum. If it is, the integer replaces the current maximum. The maximum is then added to the result vector. This continues until the end of the input vector.

The main function tests the rolling_max function by providing it with a vector of integers. It then prints the resulting vector of maximum elements found in the sequence.
*/
/*
E:
The code provided is in C++ and it correctly implements the rolling maximum function. It iterates over the input vector of integers, keeping track of the maximum element found so far. It then returns a vector containing the maximum element found at each point in the sequence.
*/

/*
P:
The problem statement asks to generate a vector of rolling maximum elements from a given vector of integers. The maximum element is calculated from the beginning of the vector up to the current position. The resulting vector is then returned.
*/

/*
I:
The input is a vector of integers. The output is also a vector of integers, where each integer is the maximum element found in the input vector up to that point.
*/

/*
C:
The constraints of the problem are that the