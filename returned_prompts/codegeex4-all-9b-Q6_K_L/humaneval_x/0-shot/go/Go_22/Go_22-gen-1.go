To filter a list of any values for integers, you can use the built-in `IsInteger()` function in JavaScript. This function will check if a value is an integer. Here's an example of how you can use it:

```javascript
function FilterIntegers(values) {
  return values.filter(function(value) {
    return Number.isInteger(value);
  });
}
```

In this example, the `filter()` method is used to create a new array that only includes the values that pass the test implemented by the provided function. The `Number.isInteger()` function is used to check if a value is an integer.

Here's how you can use the `FilterIntegers()` function:

```javascript
var values = [1, 2, 3, 'abc', {}, [], NaN, Infinity, -0, 0, '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '