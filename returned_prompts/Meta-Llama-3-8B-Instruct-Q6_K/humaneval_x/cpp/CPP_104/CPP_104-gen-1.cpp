    vector<int> result;
    for(int i = 0; i < x.size(); i++){
        int num = x[i];
        bool flag = true;
        while(num > 0){
            if(num % 10 % 2 == 0){
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

int main() {
    vector<int> v = {15, 33, 1422, 1};
    vector<int> result = unique_digits(v);
    for(int i = 0; i < result.size(); i++){
        printf("%d ", result[i]);
    }
    return 0;
}

Output:
1 15 33

Explanation:
The function unique_digits takes a vector of positive integers as input and returns a sorted vector of all elements that haven't any even digit.

In the given example, the input vector is {15, 33, 1422, 1}. The function iterates over each element in the vector, checks if the element has any even digit, and if not, adds it to the result vector. The result vector is then sorted in increasing order.

The output of the function is {1, 15, 33}, which are the elements that haven't any even digit in the input vector. The function correctly identifies the elements without even digits and returns them in sorted order.