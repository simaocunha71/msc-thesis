
has_close_elements
Your for loops are backwards. You should start j at i+1, not i. You have j=i+1 and i=i+1, which makes the inner loop do nothing.

separate_paren_groups
You have a bug in the following line:
chr=paren_string[i];

This should be:
chr = paren_string[i];

truncate_number
You should use the modulo operator (%) instead of subtracting the integer part from the float number:
return number % 1;

vowels_count
This is a good use of the transform function. You should also use a switch statement instead of a series of if statements:
switch(lower[i]) {
    case 'a':
    case 'e':
    case 'i':
    case 'o':
    case 'u':
        vowels++;
        break;
}