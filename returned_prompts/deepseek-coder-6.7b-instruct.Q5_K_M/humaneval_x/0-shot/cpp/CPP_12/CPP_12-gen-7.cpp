    if(strings.empty()){
        return "";
    }

B:
    string longest = strings[0];
    for(unsigned int i = 1; i<strings.size(); i++){
        if(strings[i].length() > longest.length()){
            longest = strings[i];
        }
    }

C:
    return longest;
}

// Testing the function
int main(){
    vector<string> test1 = {};
    printf("%s\n", longest(test1).c_str()); // should print ""

    vector<string> test2 = {"a", "b", "c"};
    printf("%s\n", longest(test2).c_str()); // should print "a"

    vector<string> test3 = {"a", "bb", "ccc"};
    printf("%s\n", longest(test3).c_str()); // should print "ccc"

    return 0;
}


A: Initial condition check if the vector is empty. If it is, it returns an empty string.

B: It then goes through each string in the vector, checking if its length is greater than the current longest string. If it is, it updates the longest string.

C: Finally, it returns the longest string.
*/

// Testing the function
int main(){
    vector<string> test1 = {};
    printf("%s\n", longest(test1).c_str()); // should print ""

    vector<string> test2 = {"a", "b", "c"};
    printf("%s\n", longest(test2).c_str()); // should print "a"

    vector<string> test3 = {"a", "bb", "ccc"};
    printf("%s\n", longest(test3).c_str()); // should print "ccc"

    return 0;
}

// This code will test the function longest() with three different test cases. The output is expected to be the longest string in the vector.
// If the vector is empty, the output should be an empty string.
// If the vector contains only one string, the output should be that string.
// If the vector contains more than one string, the output