
has_close_elements
You have an off-by-one error.  You are starting your inner loop at i + 1, which will never compare the last element to anything.
Also, you need to #include<algorithm> to use std::abs.  You can also make this more idiomatic by using std::transform and std::distance to make the loop a bit more readable.
for (int i = 0; i < numbers.size(); ++i) {
    for (int j = i + 1; j < numbers.size(); ++j) {
        if (std::abs(numbers[i] - numbers[j]) < threshold) {
            return true;
        }
    }
}

separate_paren_groups
You have a bug.  You are checking if level == 0 and if it is, you add the current_paren to the vector and reset current_paren.  However, you are doing this before adding the ')', which will result in a missing parenthesis in your string.  You need to add the ')' before adding the string to the vector.
for (int i = 0; i < paren_string.length(); ++i) {
    char chr = paren_string[i];
    if (chr == '(') {
        ++level;
        current_paren += chr;
    } else if (chr == ')') {
        --level;
        current_paren += chr;
        if (level == 0) {
            all_parens.push_back(current_paren);
            current_paren.clear();
        }
    }
}

truncate_number
You don't need to include <math.h> to use floor.  You can use std::floor instead.
return number - std::floor(number);

parse_music
You have a bug.  If the input string is empty, you will get a segmentation fault because you are trying to access music_string[i - 1] when i is 0.  You need to