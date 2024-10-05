
I'm not sure whether this is a review or a correction, but I'll try to help you out either way.
Firstly, you should note that there's a lot of repetition in your code. The first two questions are very similar in structure, and the third question is very similar to the first. In fact, the first three questions are all variations on a theme of sorting a collection of numbers. It would be beneficial to reduce this repetition by creating a function that can handle all three cases.
Secondly, your code is not very readable. The variable names are not very descriptive, and your code does not contain any comments. This makes it difficult for others to understand your code. It would be beneficial to add comments to explain what your code is doing, and to use more descriptive variable names.
Thirdly, your code is not very efficient. For example, in the first question, you are using a nested for loop to compare all pairs of numbers. This is not necessary. You can simply sort the vector of numbers and then check for consecutive numbers that are within the given threshold.
Lastly, your code is not very robust. For example, in the second question, you are assuming that the input string will always contain balanced parentheses. However, this is not a valid assumption. It would be better to add some error checking to ensure that the input string is valid.
Here's an updated version of your code that addresses these issues:
#include<stdio.h>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;

// Helper function to sort a vector of numbers in ascending order
void sort_vector(vector<float>& numbers) {
    sort(numbers.begin(), numbers.end());
}

// Helper function to sort a vector of numbers in descending order
void reverse_sort_vector(vector<float>& numbers) {
    sort(numbers.begin(), numbers.end());
    reverse(numbers.begin(), numbers.end());
}

// Main function to check if any two numbers in a vector are closer than a given threshold
bool has_close_elements(vector<float> numbers, float threshold) {
    sort_vector(numbers);
    for (int i = 0; i <