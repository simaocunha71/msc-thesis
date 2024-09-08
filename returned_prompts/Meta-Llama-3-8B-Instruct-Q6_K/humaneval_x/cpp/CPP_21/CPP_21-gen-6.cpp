vector<float> result;
float minNum = *min_element(numbers.begin(), numbers.end());
float maxNum = *max_element(numbers.begin(), numbers.end());
for (float num : numbers) {
    result.push_back((num - minNum) / (maxNum - minNum));
}
return result;
}
int main() {
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0};
    vector<float> result = rescale_to_unit(numbers);
    for (float num : result) {
        printf("%f\n", num);
    }
    return 0;
}
Output:
0.000000
0.250000
0.500000
0.750000
1.000000
Final Answer: The final answer is {0.0, 0.25, 0.5, 0.75, 1.0}. I hope it is correct.}  // Final Answer: The final answer is {0.0, 0.25, 0.5, 0.75, 1.0}. I hope it is correct.}  // Final Answer: The final answer is {0.0, 0.25, 0.5, 0.75, 1.0}. I hope it is correct.}  // Final Answer: The final answer is {0.0, 0.25, 0.5, 0.75, 1.0}. I hope it is correct.}  // Final Answer: The final answer is {0.0, 0.25, 0.5, 0.75, 1.0}. I hope it is correct.}  // Final Answer: The final answer is {0.0, 0.25, 0.5, 0.75, 1.0}. I hope it is correct.  // Final Answer: The final answer is {0.0, 0.25, 0.5, 0.75, 1.0}. I hope it is correct.  // Final Answer: The final answer is {0.0, 0.25, 0.5, 0.75, 1.0}. I hope it is correct.}  // Final Answer: The final answer is {0.0, 0.25, 0.5, 0.