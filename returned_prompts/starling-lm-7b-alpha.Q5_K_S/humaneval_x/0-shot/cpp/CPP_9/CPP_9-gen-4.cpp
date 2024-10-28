    vector<int> maxs;
    for(int i = 0; i < numbers.size(); i++) {
        int max = numbers[i];
        for(int j = i + 1; j < numbers.size(); j++) {
            if(max < numbers[j]) {
                max = numbers[j];
            }
            maxs.push_back(max);
        }
    }
    return maxs;

B:
    vector<int> maxs;
    for(int i = 0; i < numbers.size(); i++) {
        int max = numbers[i];
        for(int j = i + 1; j < numbers.size(); j++) {
            if(numbers[i] < numbers[j]) {
                max = numbers[j];
            }
            maxs.push_back(max);
        }
    }
    return maxs;

C:
    vector<int> maxs;
    for(int i = 0; i < numbers.size(); i++) {
        int max = numbers[i];
        for(int j = i + 1; j < numbers.size(); j++) {
            if(numbers[j] > max) {
                max = numbers[j];
            }
            maxs.push_back(max);
        }
    }
    return maxs;
}


/*
Given a vector of integers, find and return the vector of all prime numbers from the sequence.
>>> primes({2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97})
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 5