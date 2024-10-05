
has_close_elements
The first thing I notice is that your function has a single label A. It's not clear why you have it, but it's not needed and can be removed.
You should also use a range-based for loop here. This will make your code much more readable:
for (auto i = 0; i < numbers.size(); ++i) {
    for (auto j = i + 1; j < numbers.size(); ++j) {
        // ...
    }
}

separate_paren_groups
There are a couple of issues with your function. First, you're not handling the case where the string doesn't contain a balanced set of parentheses. You should add some checks for this and throw an exception if the input string is not valid.
Second, you're not checking whether the input string is actually a string of parentheses. This could be done using a regular expression, but that's outside the scope of this question.
Finally, you're not returning anything if no groups are found. This will result in an undefined behaviour. You should return an empty vector in this case.
truncate_number
You're using the wrong function to convert the number to an integer. You should be using floor, not int:
return number - floor(number);

words_in_sentence
Your function is a bit more complicated than it needs to be. You're checking whether a character is a space or a letter, but there's no need to do this. You can just use the isalpha function to check if a character is a letter.
Also, your loop has a bug. You're checking for spaces before letters, so if a string starts with a space, it will be skipped over. You should check for letters before spaces.
Here's a simplified version of your function