int num_apples;
int num_oranges;
int num_mangoes;

for(int i = 0; i < s.length(); i++){
if(s[i] == 'a'){
num_apples = i;
break;
}
}

for(int i = num_apples; i < s.length(); i++){
if(s[i] == 'o'){
num_oranges = i;
break;
}
}

num_mangoes = n - num_apples - num_oranges;
return num_mangoes;
}


/*

In this program, we have a function that takes a string and an integer as its arguments.
The string represents a number of apples and oranges that are distributed in a basket of fruit.
The integer represents the total number of the fruits in the basket.

We start by initializing three variables: num_apples, num_oranges, and num_mangoes.
We use a for loop to iterate through the characters of the string to find the index of the first letter 'a' (representing apples).
We break out of the loop once we find the index of the first 'a' and assign it to num_apples.

Next, we use another for loop to iterate through the remaining characters of the string to find the index of the first letter 'o' (representing oranges).
We break out of the loop once we find the index of the first 'o' and assign it to num_oranges.

Finally, we calculate the number of mangoes by subtracting the number of apples and oranges from the total number of fruits. We return this value.

This function can be used to calculate the number of mangoes in a basket of fruit given a string representing the number of apples and oranges, and an integer representing the total number of fruits in the basket.










































































