
has_close_elements
There is a bug in your code. You start comparing from the first element, but then you compare the second element with all elements that come after it, including the first one. Since you start the inner loop at i+1, the first element is not included in the comparison at all. This means that it is possible for the first element to be closer to any of the other elements than the threshold, but you will never check that.
To fix this, you should start the inner loop at i+1, but you also need to check the first element against all elements that come before it, including the last one. You can do this by adding an additional loop that iterates backwards over the array.
Here is the corrected code:
for (i = 0; i < numbers.size(); i++) {
    for (j = i + 1; j < numbers.size(); j++) {
        if (abs(numbers[i] - numbers[j]) < threshold) {
            return true;
        }
    }
    for (j = numbers.size() - 1; j > i; j--) {
        if (abs(numbers[i] - numbers[j]) < threshold) {
            return true;
        }
    }
}
return false;

separate_paren_groups
Your code is mostly correct, but there is a bug. You are adding the closing parenthesis to the current_paren string when you encounter it, but you are not checking whether the level is zero before adding it. This means that if there are any closing parentheses in the input string that are not matched by an opening parenthesis, they will be added to the current_paren string, which will cause the function to return incorrect results.
To fix this, you should check the level before adding the closing parenthesis to the current_paren string. Here is the corrected code:
if (chr == '(') {
    level += 1;
    current