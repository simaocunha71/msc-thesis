
In the first question, you have to check if the distance is less than or equal to the threshold.
Change 
if (distance < threshold) return true;
to 
if (distance <= threshold) return true;

In the second question, you have to check if the number of opening parentheses is equal to the number of closing parentheses.
Change 
if (current_depth == 0) {
    result.add(current_string.toString());
    current_string.setLength(0);
}
to 
if (current_depth == 0 && current_string.length() > 0) {
    result.add(current_string.toString());
    current_string.setLength(0);
}

In the third question, the formula to check if a triangle is right angled is wrong. You have to check if the square of the largest side is equal to the sum of the squares of the other two sides.
Change 
return max * max == a * a + b * b + c * c - max * max;
to 
return max * max == a * a + b * b + c * c - 2 * max * max;