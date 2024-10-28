Here is the JavaScript code that implements the described functionality:

```javascript
function byLength(arr) {
    // Filter out numbers outside the range 1-9
    const filteredArr = arr.filter(num => num >= 1 && num <= 9);
    
    // Sort the filtered array
    filteredArr.sort((a, b) => a - b);
    
    // Reverse the sorted array
    filteredArr.reverse();
    
    // Replace each digit with its corresponding name
    const result = filteredArr.map(num => {
        switch (num) {
            case 1: return "One";
            case 2: return "Two";
            case 3: return "Three";
            case 4: return "Four";
            case 5: return "Five";
            case 6: return "Six";
            case 7: return "Seven";
            case 8: return "Eight";
            case 9: return "Nine";
            default: return "";
        }
    });
    
    return result;
}
```

You can test the function with the provided examples:

```javascript
console.log(byLength([2, 1, 1, 4, 5, 8, 2, 3])); // Output: ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
console.log(byLength([])); // Output: []
console.log(byLength([1, -1, 55])); // Output: ["One"]
```