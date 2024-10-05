
I'll start by addressing your function prototypes.  While they are correct, they are a little on the long side.
For has_close_elements, you could do:
bool has_close_elements(const vector<float>& numbers, float threshold);

This has a few advantages:

You don't have to copy the vector, you can simply pass a pointer to it
You can't modify the vector, which is safer
You can't accidentally pass a non-vector to it, which is safer

For separate_paren_groups, you could do:
vector<string> separate_paren_groups(const string& paren_string);

This has the advantages of the above, except you can't modify the string.

truncate_number is fine as it is.  It doesn't need to change.

Your histogram function has a few problems.  The first is that you are using a string instead of a map to store the letters.  You should use a map to store the letters, and then you can iterate over it to get the counts.  Here is how you could do it:
map<char,int> histogram(const string& test){
    map<char,int> all_letters;
    for (char chr : test) {
        all_letters[chr]++;
    }
    return all_letters;
}

This has the advantage of being much simpler and easier to understand.