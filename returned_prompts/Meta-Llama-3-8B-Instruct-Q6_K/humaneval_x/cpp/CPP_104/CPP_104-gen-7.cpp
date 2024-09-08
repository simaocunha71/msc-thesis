    vector<int> result;
    for(int i = 0; i < x.size(); i++){
        int num = x[i];
        bool flag = true;
        while(num > 0){
            int digit = num % 10;
            if(digit % 2 == 0){
                flag = false;
                break;
            }
            num /= 10;
        }
        if(flag){
            result.push_back(x[i]);
        }
    }
    sort(result.begin(), result.end());
    return result;
}

int main(){
    vector<int> x = {15, 33, 1422, 1};
    vector<int> y = unique_digits(x);
    for(int i = 0; i < y.size(); i++){
        printf("%d ", y[i]);
    }
    printf("\n");
    return 0;
}

Output:
1 15 33
*/



Explanation: 

The problem requires us to create a function that takes a vector of positive integers as input and returns a sorted vector of all elements that don't have any even digits.

We iterate through each number in the input vector, and for each number, we check if it has any even digits. If it doesn't, we add it to our result vector. After adding all the numbers without even digits to the result vector, we sort the result vector in increasing order and return it.

In the main function, we create a vector of positive integers, call the unique_digits function with this vector as input, and print the result. The output is a sorted vector of all elements that don't have any even digits. 

The time complexity of this solution is O(n*m), where n is the number of elements in the input vector and m is the maximum number of digits in any of the elements. This is because we are iterating through each element in the input vector and for each element, we are checking each digit. The space complexity is O(n), where n is the number of elements in the input vector, because we are storing the result in a vector. 

The function is implemented in C++ and uses the standard library for vector and algorithm. The sort function is used to sort the result vector in increasing order. The printf function is used to print the result. 

The output of the program is a sorted vector of all elements that don't have any even digits. In this case, the output is {1, 15, 33}. 

This solution is efficient and scalable, as it can handle large input