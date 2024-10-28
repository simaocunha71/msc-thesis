
The first question has a bug, where the loop starts at i=0. That means the last element is never compared to anything. It should start at i=1 instead.
Also, the condition to return false should be when numbers[i]-numbers[j] >= threshold, since you are looking for numbers that are less than threshold apart.

The second question has a bug, where it does not check if the string is empty before trying to access the first character. This will lead to undefined behaviour.
Also, the loop should start at i=0, not i=1.

The third question is missing a return statement.

The fourth question is missing a return statement.

The fifth question is missing a return statement.