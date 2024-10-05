
First, let's go through the style and formatting of your code, then I'll go over the logic of each function.
Style and Formatting
The code you have posted is pretty clean, but there are a few things that you can do to make it even better.
1. Use spaces around operators. This makes the code easier to read. For example, change:
if (abs(numbers[i]-numbers[j])<threshold)

to:
if (abs(numbers[i] - numbers[j]) < threshold)

2. Use braces even for single-line if statements. This makes the code more consistent and easier to read. For example, change:
if (chr=='(')
{
    level+=1;
    current_paren+=chr;
}

to:
if (chr == '(') {
    level += 1;
    current_paren += chr;
}

3. Use camelCase for variable names. This is the standard naming convention for variables in C++. For example, change:
vector<float> numbers

to:
std::vector<float> numbers

4. Use std::endl instead of \n. This is the standard way to output a newline in C++. For example, change:
printf("%d\n", i);

to:
std::cout << i << std::endl;

5. Use the auto keyword for variable declarations. This can make the code more readable and easier to maintain. For example, change:
vector<int> result = {0,0};

to:
auto result = std::vector<int>{0, 0};

Now let's go over the logic of each function.
has_close_elements
The has_close_elements function is supposed to check if any two numbers in the given vector are closer to each other than the given threshold. However,