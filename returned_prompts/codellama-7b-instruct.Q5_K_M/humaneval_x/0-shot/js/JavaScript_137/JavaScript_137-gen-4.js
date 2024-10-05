/*
  Create a function that takes in two numbers as arguments and returns the product of those two numbers.
  However, if one of the arguments is 0, the function should return 0.
  Note: You can't divide by zero!

  multiply(2, 3) ➞ 6
  multiply(3, 0) ➞ 0
  multiply(0, 3) ➞ 0
  multiply(0, 0) ➞ 0
  multiply("2", "3") ➞ "6"
  multiply("3", "0") ➞ 0
  multiply("0", "3") ➞ 0
  multiply("0", "0") ➞ 0
  multiply(2, "3") ➞ 6
  multiply("2", 3) ➞ 6
  multiply(0, "3") ➞ 0
  multiply("0", 3) ➞ 0
  multiply("2", 0) ➞ 0
  multiply(2, "0") ➞ 0
  multiply("0", "0") ➞ 0
  multiply("3", "0") ➞ 0
  multiply("0", "3") ➞ 0
  multiply("3", "2") ➞ 6
  multiply("2", "3") ➞ 6
  multiply("0", "0") ➞ 0
  multiply("2", "2") ➞ 4
  multiply("1", "1") ➞ 1
  multiply("0", "1") ➞ 0
  multiply("1", "0") ➞ 0
  multiply("0", "2") ➞ 0
  multiply("2", "0") ➞ 0
  multiply("1", "2") ➞ 2
  multiply("2", "1") ➞ 2
  multiply("2", "2") ➞ 4
  multiply("1", "1") ➞ 1
  multiply("0",