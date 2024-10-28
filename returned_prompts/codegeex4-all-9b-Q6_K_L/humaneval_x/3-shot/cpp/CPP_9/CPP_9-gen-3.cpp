
Your question is tagged C++, but you use C style for loops. You can use the range-based for loop in C++ instead of the traditional for loop:
for (float number : numbers) {
    //...
}

For the second question, you have a bug in your function. The vector all_parens is not initialized, and you push_back to it. This will cause a segmentation fault. You should add a line to initialize it:
vector<string> all_parens;

For the third question, the function truncate_number is not correct. It should return the fractional part of the number, which is number - int(number). This is because the fractional part is the part after the decimal point. You can use the fmod function to get the fractional part of a number:
return fmod(number, 1);

For the fourth question, you have a bug in your function. The variable max is not initialized, and you use it in the if statement. This will cause a segmentation fault. You should add a line to initialize it:
int max = 0;

And you should also initialize max_numbers to have the same size as numbers, so you can push_back to it:
vector<int> max_numbers(numbers.size());

Finally, you should use the auto keyword to declare variables that can be automatically deduced from their initializer. This makes your code more readable and less prone to errors. For example:
for (auto number : numbers) {
    //...
}