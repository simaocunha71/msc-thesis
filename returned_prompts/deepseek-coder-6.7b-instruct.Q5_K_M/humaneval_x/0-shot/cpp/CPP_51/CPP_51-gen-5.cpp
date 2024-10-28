    transform(text.begin(), text.end(), text.begin(), ::tolower); // convert to lowercase
    int i=0;
    while(i<text.size()){
        if(text[i]=='a' || text[i]=='e' || text[i]=='i' || text[i]=='o' || text[i]=='u'){
            text.erase(i,1);
        }else{
            i++;
        }
    }
    return text;
}


A: The problem is that you're modifying the string while iterating over it. This is not safe because it can lead to undefined behavior.
Here's a safer way to do this:
string remove_vowels(string text){
    string result;
    for(char c : text)
        if(!isVowel(c))
            result += c;
    return result;
}

bool isVowel(char c){
    c = tolower(c);
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

This code makes a copy of the string without the vowels, and it doesn't modify the original string. It also uses the tolower function to handle both uppercase and lowercase vowels.

A: Here's a version of the function that uses the standard library's erase-remove idiom to remove the vowels:
string remove_vowels(string text)
{
    text.erase(remove_if(text.begin(), text.end(), ::tolower), text.end());
    return text;
}

This code uses the std::remove_if algorithm to remove the vowels from the string, and std::erase to actually remove them. The ::tolower function is used to convert the string to lowercase before checking for vowels.

A: Here is a version of your function that uses a for loop to iterate over the string and remove the vowels:

std::string remove_vowels(std::string text) {
    for (int i = 0; i < text.size(); i++) {
