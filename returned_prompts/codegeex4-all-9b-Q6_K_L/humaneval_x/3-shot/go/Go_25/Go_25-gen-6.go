
Your solution for HasCloseElements is correct.
For SeparateParenGroups, you're missing the check if the current depth is negative. This would happen if there are unpaired close parentheses. A solution could be to return an error in this case, instead of appending an empty string to the result slice.
The implementation of TruncateNumber is correct.
For Factorize, you could optimize it by starting with i = 2 and incrementing i by 1, but I think the code is already fairly clear and easy to understand.