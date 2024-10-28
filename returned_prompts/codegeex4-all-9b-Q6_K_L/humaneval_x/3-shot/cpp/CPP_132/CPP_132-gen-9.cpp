
Q1
You're not returning anything if there are no close elements. Also, the if (abs(numbers[i]-numbers[j])<threshold) should be if (abs(numbers[i]-numbers[j])<threshold).
Q2
You're not accounting for the spaces in the input string. You should add a check to skip over them. Also, you're not handling the case where there are no parentheses in the string, which will leave current_paren as empty and cause an issue when trying to push it back.
Q3
This is fine, but you should check that number is not negative.
Q4
This is fine, but you're not checking to see if the string is balanced to begin with. You should return false if the level is not equal to 0 when you finish checking the string.