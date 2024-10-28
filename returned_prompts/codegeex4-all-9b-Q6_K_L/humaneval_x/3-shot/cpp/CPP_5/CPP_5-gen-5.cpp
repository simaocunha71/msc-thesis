
The first and third questions are fairly straightforward.  The second question is more complex because it involves string manipulation and parsing.

has_close_elements
You have a good start, but you're not keeping track of the minimum difference you've seen so far.  You also don't need to check pairs that you've already checked (i.e. (1, 2) and (2, 1)).  It's a good idea to break up your code into smaller functions, and use meaningful variable names.  I'll leave it to you to implement this.
vector<float> close_elements(vector<float> numbers, float threshold){
    float min_diff = threshold;
    for (int i=0; i<numbers.size(); i++){
        for (int j=i+1; j<numbers.size(); j++){
            float diff = abs(numbers[i]-numbers[j]);
            if (diff < min_diff){
                min_diff = diff;
            }
        }
    }
    return min_diff;
}

separate_paren_groups
Your code looks good.  I'd suggest using the string stream std::stringstream rather than concatenating strings.  It's a bit more efficient, and it's easier to read.  Here's a slightly modified version of your code:
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level=0;
    char chr;
    for (int i=0; i<paren_string.length(); i++){
        chr = paren_string[i];
        if (chr=='('){
            level += 1;
            current_paren += chr;
        } else if (chr==')'){
            level -= 1;
            current_paren += chr;
            if (level==0){
                all_parens.push_back(current_paren);
                current_paren = "";
            }
        }
    }
    return all_parens;
}

truncate_number
You're using the floor function, which returns the largest integer less than or equal to the argument.  You want the largest integer less than the argument, so you should use ceil instead.
float truncate_number(float number){
    return number - (float)ceil(number);
}

intersperse
