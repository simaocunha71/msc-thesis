  let digits = n.toString().split('');
  let product = 1;
  let flag = false;

  for (let i = 0; i < digits.length; i++) {
    if (digits[i] % 2 !== 0) {
      product *= parseInt(digits[i]);
      flag = true;
    }
  }

  return flag ? product : 0;
}

console.log(digits(1))  // 1
console.log(digits(4))  // 0
console.log(digits(235)) // 15

//The function digits converts the number to string and then splits the string into an array of digits. Then it loops over the array and multiplies the odd digits together. If no odd digit is found, it returns 0.
//The function uses a flag to check if there is at least one odd digit. If there is, it returns the product. If not, it returns 0.
//The time complexity of this function is O(n), where n is the number of digits in the input number.
//The space complexity of this function is O(n), where n is the number of digits in the input number.

//I have also done the same problem in python
//Python Code:

def digits(n):
  digits = list(str(n))
  product = 1
  flag = False

  for i in digits:
    if int(i) % 2 != 0:
      product *= int(i)
      flag = True

  return product if flag else 0

print(digits(1))  # 1
print(digits(4))  # 0
print(digits(235)) # 15

//The function digits converts the number to string and then splits the string into a list of digits. Then it loops over the list and multiplies the odd digits together. If no odd digit is found, it returns 0.
//The function uses a flag to check if there is at least one odd digit. If there is, it returns the product. If not, it returns 0.
//The time