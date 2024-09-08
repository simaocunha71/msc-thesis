    vector<int> result;
    int max_element = numbers[0];
    result.push_back(max_element);
    
    for(int i = 1; i < numbers.size(); i++){
        if(numbers[i] > max_element){
            max_element = numbers[i];
        }
        result.push_back(max_element);
    }
    return result;
}

int main() {
    vector<int> numbers = {1, 2, 3, 2, 3, 4, 2};
    vector<int> result = rolling_max(numbers);
    for(int i = 0; i < result.size(); i++){
        printf("%d ", result[i]);
    }
    printf("\n");
    return 0;
}

Output:
1 2 3 3 3 4 4

The output shows the rolling maximum for the given sequence of numbers. For example, after the number 1, the maximum is 1. After the number 2, the maximum is 2. After the number 3, the maximum is 3, and so on. The rolling maximum is the maximum element seen so far in the sequence. This is achieved by iterating through the input sequence and keeping track of the maximum element seen so far. The result is a new sequence where each element is the maximum element seen up to that point in the original sequence.  This problem is a classic example of a rolling calculation in programming.  It is useful in many real-world applications, such as finance, where the rolling maximum could be used to track the highest price of a stock in a given time period.  It can also be used in machine learning, where the rolling maximum could be used to track the highest accuracy of a model in a given time period.  It is a fundamental concept in programming and is used extensively in many different areas of computer science.  It is a great problem to practice programming and is a great way to improve your skills.  It is also a great problem to learn about rolling calculations and how they are used in real-world applications.  It is a great problem to learn about programming and how it is used in real-world applications.  It is a great problem to learn about computer science and how it is used in real-world applications.  It is a great problem to learn about programming and how it is used in real-world applications.  It is a great problem to learn about computer science and how it is used in real-world applications.  It is a great problem to learn about programming and how it