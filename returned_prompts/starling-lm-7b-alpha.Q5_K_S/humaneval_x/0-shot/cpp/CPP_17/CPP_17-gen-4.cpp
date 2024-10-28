    vector<int>res;
    int i = 0;
    while(i<music_string.size()) {
        if(music_string[i] == 'o') {
            res.push_back(4);
            i += 1;
        } else if(music_string[i] == 'o' && music_string[i+1] == '|') {
            res.push_back(2);
            i += 2;
        } else if(music_string[i] == '.' && music_string[i+1] == '|') {
            res.push_back(1);
            i += 2;
        }
    }
    return res;
}




/*
In this code, I used the following logic to parse the string and generate vector of integers:

1. I used a while loop to iterate over the input string.
2. In the while loop, I used if-else if conditions to identify the note type.
3. Depending on the note type, I pushed the corresponding value to the result vector.
4. I incremented the index i to move to the next character in the string.
5. I repeated step 2-4 until all the characters in the input string are processed.
6. Finally, I returned the result vector.

The time complexity of this code is O(n), where n is the length of the input string.
The space complexity of this code is O(n), where n is the length of the result vector.

The code assumes that the input string is valid and does not contain any special characters or whitespaces.
It also assumes that the input string is in the correct format as described in the problem statement.

Overall, this code provides a simple and efficient solution to parse the input string and generate the result vector.

*/



























































































