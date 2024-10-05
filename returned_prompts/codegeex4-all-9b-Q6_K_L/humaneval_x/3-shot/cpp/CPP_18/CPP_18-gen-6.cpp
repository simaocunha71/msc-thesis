
The first problem that stands out in the code is the lack of braces around the statements in the for loop. This is a common mistake when you're transitioning between languages, and it's easy to miss. In C++, you're required to use braces to define the scope of the loop.
For instance, the first problem is with the following code:
for (i=0;i<numbers.size();i++)
for (j=i+1;j<numbers.size();j++)
if (abs(numbers[i]-numbers[j])<threshold)
return true;

return false;

This should be rewritten as:
for (i=0;i<numbers.size();i++) {
    for (j=i+1;j<numbers.size();j++) {
        if (abs(numbers[i]-numbers[j])<threshold) {
            return true;
        }
    }
}

return false;

The second problem is with the following code:
for (i=0;i<paren_string.length();i++) {
    chr=paren_string[i];
    if (chr=='(') {
        level+=1;
        current_paren+=chr;
    }
    if (chr==')') {
        level-=1;
        current_paren+=chr;
        if (level==0){
            all_parens.push_back(current_paren);
            current_paren="";
        }
    }
}

This should be rewritten as:
for (i=0;i<paren_string.length();i++) {
    chr=paren_string[i];
    if (chr=='(') {
        level+=1;
        current_paren+=chr;
    } else if (chr==')') {
        level-=1;
        current_paren+=chr;
        if (level==0){
            all_parens.push_back(current_paren);
            current_paren="";
        }
    }
}

The third problem is with the following code:
for (i=0;i<str_length;i++) {
    if (str[i]==substring[0]) {
        for (j=