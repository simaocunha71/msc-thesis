
The first question is correct. The second question has a bug. The logic should be: 
if (c == ')') {
    current_depth -= 1;
    current_string.append(c);
    if (current_depth == 0) {
        result.add(current_string.toString());
        current_string.setLength(0);
    }
}

The third question has a bug. The logic should be: 
return number - (int)number;

The fourth question has a bug. The logic should be:
if (a*a + b*b == c*c || a*a + c*c == b*b || b*b + c*c == a*a) return true;
return false;