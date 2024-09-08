    vector<int> result;
    for(int i = 0; i < numbers.size(); i++){
        result.push_back(numbers[i]);
        if(i < numbers.size() - 1){
            result.push_back(delimeter);
        }
    }
    return result;
} 

Example usage:
int main() {
    vector<int> numbers = {1, 2, 3};
    int delimeter = 4;
    vector<int> result = intersperse(numbers, delimeter);
    for(int num : result){
        printf("%d ", num);
    }
    printf("\n");
    return 0;
}

Output:
1 4 2 4 3
Explanation:
This function takes a vector of integers and an integer as input. It creates a new vector and iterates over the input vector. For each element, it adds the element to the result vector and then checks if it's not the last element. If it's not the last element, it adds the delimeter to the result vector. Finally, it returns the result vector. 

The example usage demonstrates how to use this function. It creates a vector of integers {1, 2, 3} and an integer 4 as the delimeter. It then calls the function with these inputs and prints the result. The output is {1, 4, 2, 4, 3}. 
Final Answer: The final answer is intersperse. I hope it is correct. 





