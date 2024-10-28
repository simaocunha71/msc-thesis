//create a dictionary with letters as keys and a value of 0
let histogram = {};

//split the string into an array of letters
let letters = test.split(" ");

//loop through the array
for(let i = 0; i < letters.length; i++) {
  //if the letter is in the dictionary, increment the counter, else set to 1
  if(histogram[letters[i]]) {
    histogram[letters[i]]++;
  } else {
    histogram[letters[i]] = 1;
  }
}

//create an object to store the max value and the key
let max = {
  value: 0,
  key: ""
};

//loop through the dictionary to find the max value
for(let key in histogram) {
  if(histogram[key] > max.value) {
    max.value = histogram[key];
    max.key = key;
  }
}

//if there are multiple values with the same max, create an array to store all keys
if(max.value > 1) {
  max.key = [max.key];
}

//return the max value and key
return max;

};

