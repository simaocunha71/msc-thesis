
In has_close_elements, you're going to have trouble with your loop's termination condition.  You'll have j go past the end of the vector, which will cause an out-of-bounds access and crash your program.  You need to fix the loop to be:
for (i = 0; i < numbers.size() - 1; i++) {
    for (j = i + 1; j < numbers.size(); j++) {
        // ...
    }
}

In separate_paren_groups, you're not handling the case where there are no open parentheses.  That's going to cause a crash.  You need to add a check at the top of the function to ensure that there are at least one open and one close parenthesis.  If not, return an empty vector.
In exchange, you're not checking whether lst2 is empty.  This will cause a crash if it is.  You need to add a check at the top of the function to ensure that lst2 is not empty.  If it is, return "NO".