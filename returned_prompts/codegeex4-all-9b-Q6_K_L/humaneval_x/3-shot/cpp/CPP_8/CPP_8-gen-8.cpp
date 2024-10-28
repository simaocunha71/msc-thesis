
Your first function seems fine, but you could avoid the variable j and do:
for (auto i : numbers) {
    for (auto j : numbers) {
        // rest of the code
    }
}

Your second function seems fine as well, but you could use a range-based for loop for the string as well:
for (auto chr : paren_string) {
    // rest of the code
}

Your third function seems fine as well, but you could use the fmod function to get the decimal part of the number:
return fmod(number, 1);

Your fourth function seems fine as well, but you could use the accumulate function to get the sum and product of the numbers:
int sum = accumulate(numbers.begin(), numbers.end(), 0);
int product = accumulate(numbers.begin(), numbers.end(), 1, multiplies<int>());

You could then return the vector with the sum and product:
vector<int> result = {sum, product};
return result;