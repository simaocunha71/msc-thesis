    let regex = /^[a-zA-Z]\w*(\.\w*$|\.\w*[a-zA-Z])$/;
    return regex.test(file_name);
};




/*
 Create a function which takes two strings, and returns 'Yes' if one of the strings is the other's reverse,
 otherwise returns 'No'.
 Examples:
 areSame("abcde","edcba") # => 'Yes'
 areSame("abcde","abcde") # => 'No'
 areSame("abcde","cdeab") # => 'No'
*/
const areSame = (str1, str2) => {
    return str1 === str2.split("").reverse().join("");
};




/*
 Create a function which takes a number n, and returns the sum of all the numbers from 1 to n,
 including n.
 Examples:
 sum(5) # => 15
 sum(10) # => 55
 sum(100) # => 5050
*/
const sum = (n) => {
    return n * (n + 1) / 2;
};




/*
 Create a function which takes a string representing a file's path, and returns true if the file exists,
 otherwise returns false.
 Examples:
 exists("file.txt") # => true
 exists("nonExistentFile.txt") # => false
 exists("C:\\myFolder\\file.txt") # => true
*/
const exists = (file_path) => {
    try {
        require(file_path);
        return true;
    } catch (e) {
        return false;
    }
};




/*
 Create a function which takes an array of strings, and returns a new array containing only the strings with length less than or equal to the given number.
 Examples:
 filterShortStrings(["hello", "world", "!!!", "!!!"], 3) # => ["hello", "world"]
 filterShortStrings(["hello", "world"], 3) # => ["hello", "world"]
 filterShortStrings(["hello", "world"], 5) # => ["hello", "world"]
*/
const