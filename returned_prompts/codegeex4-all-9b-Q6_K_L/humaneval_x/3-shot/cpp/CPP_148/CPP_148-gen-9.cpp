
The first function has a potential out-of-bounds bug. It should be:
for (i=0;i<numbers.size()-1;i++) // -1 to prevent out-of-bounds access
for (j=i+1;j<numbers.size();j++)

The second function has a bug. It will miss the last parentheses group if there is no closing parentheses. A better way to check the parentheses is to use a stack. If the stack is empty when a closing parentheses is encountered, then we know that there is a bug in the parentheses.

The third function can be simplified by using the fmod function instead of subtracting the integer part from the float. fmod returns the remainder of the division of number by 1.
float truncate_number(float number){
    return fmod(number, 1);
}

The fourth function can be simplified by using the find function to search for the planet names in the all_planets vector. If the planet name is not found, then the find function will return the end iterator of the vector. We can use the distance function to find the index of the planet in the all_planets vector.
vector<string> bf(string planet1, string planet2){
    vector<string> all_planets;
    all_planets.push_back("Mercury");
    all_planets.push_back("Venus");
    all_planets.push_back("Earth");
    all_planets.push_back("Mars");
    all_planets.push_back