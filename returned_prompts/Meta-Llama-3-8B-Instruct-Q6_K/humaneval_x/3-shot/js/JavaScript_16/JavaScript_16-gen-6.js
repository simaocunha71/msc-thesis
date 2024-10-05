  return new Set(string.toLowerCase().split('')).size;
}
// Set is a collection of unique elements. When you use the Set() function to create a new set, 
// it automatically removes any duplicate elements. So, it will return the number of distinct characters. 
// The toLowerCase() function is used to make the function case-insensitive. 
// The split('') function splits the string into a list of characters, and the size property of the Set gives the number of distinct characters.