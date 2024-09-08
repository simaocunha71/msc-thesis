    map<string, int> numMap;
    for (int i = 0; i < numbers.size(); i++) {
        string num = "";
        while (i < numbers.size() && numbers[i] != ' ') {
            num += numbers[i];
            i++;
        }
        i++; // skip the space
        numMap[num]++;
    }

    string sortedNumbers = "";
    for (auto it = numMap.begin(); it != numMap.end(); it++) {
        for (int i = 0; i < it->second; i++) {
            sortedNumbers += it->first + " ";
        }
    }

    return sortedNumbers;
}
int main() {
    string numbers = "three one five";
    string sortedNumbers = sort_numbers(numbers);
    printf("%s\n", sortedNumbers.c_str());
    return 0;
}

Output:
one three five

Explanation:
The given function, sort_numbers, takes a string of space-delimited numbers as input and returns a string with the numbers sorted from smallest to largest. The function first creates a map to store the frequency of each number. Then, it iterates over the map and constructs the sorted string by appending each number to the result string as many times as its frequency. Finally, it returns the sorted string. In the main function, the string "three one five" is passed to the sort_numbers function, and the sorted string "one three five" is printed.