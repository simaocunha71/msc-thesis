    vector<string> res;
    int len = str.length();
    for(int i=0; i<len; i++){
        res.push_back(str.substr(0,i+1));
    }
    return res;
}


int main(){
    string str = "abc";
    vector<string> prefixes = all_prefixes(str);
    for(int i=0; i<prefixes.size(); i++){
        printf("%s\n", prefixes[i].c_str());
    }
    return 0;
}

// Output:
// a
// ab
// abc


*/

// The code provided is a C++ solution for the above question. It uses the concept of strings in C++ and the function substr() to find the prefixes. It then returns these prefixes in a vector.

// In the function all_prefixes(), it first initializes an empty vector of strings. Then it uses a for loop to iterate through each character in the input string. For each iteration, it uses the substr() function to extract a substring from the start of the string up to the current index. This substring is then added to the vector. The function finally returns the vector of all prefixes.

// In the main() function, it tests the all_prefixes() function with the string "abc". It then prints out the prefixes.


// It's important to note that the time complexity of this solution is O(n^2) because of the substr() function in the loop. This means that the time it takes to run increases quadratically with the size of the input string. This is because substr() creates a new string and copies the characters from the original string to the new string, which takes O(n) time.

// Also, the space complexity is O(n) because we are storing each prefix in the result vector.



/*

// You can also use C++11 range-based for loop to simplify the code:

vector<string> all_prefixes(string str){
    vector<string> res;
    for(int i=0; i<str.length(); i++){
        res.push_back(str.substr(0,i+