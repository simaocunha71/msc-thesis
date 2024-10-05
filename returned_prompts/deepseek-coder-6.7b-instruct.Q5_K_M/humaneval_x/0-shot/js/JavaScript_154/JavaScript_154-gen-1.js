const rotate = (str) => {
    return str.slice(1) + str[0];
};

const checkAllRotations = (a, b) => {
    for (let i = 0; i < b.length; i++) {
        if (a.includes(b)) {
            return true;
        }
        b = rotate(b);
    }
    return false;
};

return checkAllRotations(a, b);
};
console.log(cycpatternCheck("abcd","abd")); //false
console.log(cycpatternCheck("hello","ell")); //true
console.log(cycpatternCheck("whassup","psus")); //false
console.log(cycpatternCheck("abab","baa")); //true
console.log(cycpatternCheck("efef","eeff")); //false
console.log(cycpatternCheck("himenss","simen")); //true

//This solution creates a function rotate that rotates a string by one character to the left.
//Then it creates a function checkAllRotations that checks if string b is a substring of string a, 
//if not, it rotates b by one character and checks again.
//If at any point b is a substring of a, the function returns true. If the function goes through all rotations without finding a match, it returns false.
//The time complexity of the solution is O(n*m) where n is the length of the first string and m is the length of the second string.
//The space complexity is O(1) as it only uses a constant amount of space.
//It checks all rotations of the second string and returns true if any of them are found in the first string.
//If no rotation is found, it returns false.
//It uses the JavaScript built-in method includes() to check if a substring is present in a string.
//It uses the JavaScript built-in method slice() to rotate the string.
//It uses a loop to check all rotations.
//It uses an if statement to check if the substring is a substring of the string.
//It uses a return statement to return the result.
//It uses a function declaration to define the function.
//It uses arrow function syntax to