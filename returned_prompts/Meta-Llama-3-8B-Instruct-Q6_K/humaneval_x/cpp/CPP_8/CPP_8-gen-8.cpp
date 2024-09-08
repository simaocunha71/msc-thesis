    if(numbers.empty()){
        return {0, 1};
    }

    int sum = 0;
    int product = 1;

    for(int i = 0; i < numbers.size(); i++){
        sum += numbers[i];
        product *= numbers[i];
    }

    return {sum, product};
}

int main()
{
    vector<int> numbers = {1, 2, 3, 4};
    vector<int> result = sum_product(numbers);
    cout << result[0] << " " << result[1] << endl;
    return 0;
}

Output:
10 24

Explanation: The code defines a function sum_product that calculates the sum and product of a given vector of integers. If the vector is empty, it returns {0, 1}. Otherwise, it iterates over the vector, adding each number to the sum and multiplying each number by the product. Finally, it returns a vector containing the sum and product. In the main function, it creates a vector of integers {1, 2, 3, 4}, calls the sum_product function, and prints the result. The output is 10 and 24, which are the sum and product of the given vector, respectively.