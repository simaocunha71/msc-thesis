
I'm going to start with the first one. It's a bit hard to tell exactly what your problem is, because you haven't actually asked a question, but I'm going to assume you want to know how to complete the function.

Your function has a type signature of
bool has_close_elements(vector<float> numbers, float threshold);

This tells us that your function takes two arguments: a vector of floats, and a float, and returns a boolean.
You want to iterate over all pairs of numbers in the vector, and return true if any pair is within the given threshold of each other. If you get through all pairs without finding any that are close enough, you should return false.
The function has a for-loop which correctly iterates over all pairs of numbers in the vector. It also correctly checks whether the current pair is within the given threshold of each other. The problem is that your function is returning true as soon as it finds one pair of numbers that are close enough, but it should only return true if it finds a pair of numbers that are close enough and it's gone through all of the pairs.
To fix this, you should replace the return true in the inner loop with a break statement. This will exit the inner loop, but not the outer loop, so your function will continue to check the rest of the pairs.
Here's the corrected function:
bool has_close_elements(vector<float> numbers, float threshold){
    for (int i=0; i<numbers.size(); i++) {
        for (int j=i+1; j<numbers.size(); j++) {
            if (abs(numbers[i]-numbers[j])<threshold) {
                break;
            }
        }
    }
    return false;
}

Now let's move on to the second question. Again, I'm going to assume you want to know how to complete the function.

Your function has a type signature of
vector<string> separate_paren_groups(string paren_string);

This tells us that your function takes a single argument: a string, and returns a vector of strings.
You want to separate the input string into groups of nested parentheses, and return the vector of those groups.
The function has a for-loop which correctly iterates over each character in the