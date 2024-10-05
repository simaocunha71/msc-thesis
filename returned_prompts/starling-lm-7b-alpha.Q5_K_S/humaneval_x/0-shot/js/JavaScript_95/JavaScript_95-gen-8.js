
// First, we need to check if the given dictionary is empty. If it is, we can immediately return false.
if (Object.keys(dict).length === 0) {
    return false;
}

// Next, we can iterate over each key in the dictionary to check its case. We can use the Object.keys method to get an array of all keys in the dictionary.
const keyArray = Object.keys(dict);

// We can use the some method to check if there is at least one key in the dictionary that is not in either lower or upper case.
const isLower = keyArray.some(key => {
    return dict[key].toLowerCase() !== dict[key];
});

const isUpper = keyArray.some(key => {
    return dict[key].toUpperCase() !== dict[key];
});

// If isLower is true, it means that there is at least one key in the dictionary that is not in lower case. If isUpper is true, it means that there is at least one key in the dictionary that is not in upper case. In either case, we can return false.
if (isLower || isUpper) {
    return false;
}

// If we have made it this far, it means that all keys in the dictionary are in either lower or upper case, so we can return true.
return true;
};

checkDictCase({"a":"apple", "b":"banana"}); // true
checkDictCase({"a":"apple", "A":"banana", "B":"banana"}); // false
checkDictCase({"a":"apple", 8:"banana", "a":"apple"}); // false
checkDictCase({"Name":"John", "Age":"36", "City":"Houston"}); // false
checkDictCase({"STATE":"NC", "ZIP":"12345"}); // true

*/


















































































