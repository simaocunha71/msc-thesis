/*
Write a function that accepts two vectors of strings and returns the vector that has 
total number of chars in the all strings of the vector less than the other vector.

if the two vectors have the same number of chars, return the first vector.

Examples
total_match({}, {}) ➞ {}
total_match({"hi", "admin"}, {"hI", "Hi"}) ➞ {"hI", "Hi"}
total_match({"hi", "admin"}, {"hi", "hi", "admin", "project"}) ➞