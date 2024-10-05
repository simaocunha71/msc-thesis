
// I am not happy with this solution. I think it is a bit too long and not very readable.
// Is there a better way to write it?

}

// Test Cases
// >>> SeparateParenGroups('()')
// ['()']
// >>> SeparateParenGroups('((()))')
// ['((()))']
// >>> SeparateParenGroups('((())())')
// ['((())())']
// >>> SeparateParenGroups('(((())))')
// ['(((())))']
// >>> SeparateParenGroups('(()(()))')
// ['(()(()))']
// >>> SeparateParenGroups('((((()))))')
// ['((((()))))']
// >>> SeparateParenGroups('(((((())())))')
// ['(((((())())))']
// >>> SeparateParenGroups('(((((())())))')
// ['(((((())())))']
// >>> SeparateParenGroups('(((((())())))')
// ['(((((())())))']
// >>> SeparateParenGroups('(((((())())))')
// ['(((((())())))']
// >>> SeparateParenGroups('(((((())())))')
// ['(((((())())))']
// >>> SeparateParenGroups('(((((())())))')
// ['(((((())())))']
// >>> SeparateParenGroups('(((((())())))')
// ['(((((())())))']
// >>> SeparateParenGroups('(((((())())))')
// ['(((((())())))']
// >>> SeparateParenGroups('(((((())())))')
// ['(((((())())))']
// >>> SeparateParenGroups('(((((())())))')
// ['(((((())())))']
// >>> SeparateParenGroups('(((((())())))')
// ['(((((())())))']
// >>> SeparateParenGroups('(((((())())))')
// ['(((((())())))']
// >>> SeparateParenGroups('(((((())())))')
// ['(((((