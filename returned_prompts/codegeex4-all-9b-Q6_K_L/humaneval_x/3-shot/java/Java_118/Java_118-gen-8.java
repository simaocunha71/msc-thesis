
In the first question, your code checks every pair of elements in the list. You could reduce the time complexity by checking only consecutive elements, since if the elements are not close enough, then the next pair won't be either. The code would look like this:
for (int i = 0; i < numbers.size() - 1; i++) {
    double distance = Math.abs(numbers.get(i) - numbers.get(i + 1));
    if (distance < threshold) return true;
}
return false;

In the second question, your code correctly separates the groups of parentheses, but it doesn't ignore spaces. You can remove the spaces from the input string before processing it, like this:
paren_string = paren_string.replaceAll("\\s+", "");

In the third question, your code is correct, but it can be simplified by using the built-in Math.floor() function, which returns the largest integer smaller than or equal to the given number. The code would look like this:
return Math.floor(number);

In the fourth question, your code is correct, but it can be simplified by using the built-in String.contains() method, which returns true if the string contains the given substring. The code would look like this:
String vowels = "aeiouAEIOU";
for (int i = word.length() - 2; i >= 1; i--) {
    char c = word.charAt(i);
    if (vowels.contains("" + c)) {
        return "" + c;
    }
}
return "";