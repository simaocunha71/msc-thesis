
has_close_elements

The code is fine, but a comment would be nice to explain what you're doing.  For example:
for (i = 0; i < numbers.size(); ++i)
{
    for (j = i + 1; j < numbers.size(); ++j)
    {
        if (abs(numbers[i] - numbers[j]) < threshold)
        {
            return true;
        }
    }
}

return false;

separate_paren_groups

A comment here would be nice to explain what you're doing.  Also, I'd use a for-loop instead of a while-loop:
for (int i = 0; i < paren_string.length(); ++i)
{
    chr = paren_string[i];
    if (chr == '(')
    {
        ++level;
        current_paren += chr;
    }
    else if (chr == ')')
    {
        --level;
        current_paren += chr;
        if (level == 0)
        {
            all_parens.push_back(current_paren);
            current_paren = "";
        }
    }
}

truncate_number

The name truncate_number is not very descriptive.  I'd name it something like get_fractional_part or something similar.  Also, I'd use a more descriptive name like number_value instead of number:
return number_value - static_cast<int>(number_value);

words_in_sentence

The name words_in_sentence is not very descriptive.  I'd name it something like get_words_with_prime_lengths or something similar.  Also, I'd use a more descriptive name like sentence_string instead of sentence:
string words;
string word;
for (int i = 0; i < sentence_string.length(); ++i)
{
    if (sentence_string[i] == ' ')
    {
        if (is_prime(word.length()))
        {
            words += word;
            words += ' ';
        }
        word = "";
    }
    else
    {
        word += sentence_string[i];
    }
}

if (is_prime(word.length()))
{
    words += word;
}

return words