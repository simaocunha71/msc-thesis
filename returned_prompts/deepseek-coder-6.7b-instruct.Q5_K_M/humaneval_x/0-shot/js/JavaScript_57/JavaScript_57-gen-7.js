  let increasing = true;
  let decreasing = true;
  
  for(let i = 0; i < l.length - 1; i++){
    if(l[i] > l[i + 1]) increasing = false;
    if(l[i] < l[i + 1]) decreasing = false;
  }
  
  return increasing || decreasing;
}
console.log(monotonic([1, 2, 4, 20])) // true
console.log(monotonic([1, 20, 4, 10])) // false
console.log(monotonic([4, 1, 0, -10])) // true

```

## ✍️ Conclusion

This is a simple problem of checking if an array is monotonically increasing or decreasing. By iterating through the array and checking the difference between each pair of elements, we can determine if the array is monotonically increasing or decreasing. 

The time complexity of this solution is O(n) as we are looping through the array once. The space complexity is O(1) as we are using a constant amount of space.

I hope you find this solution helpful and it serves as a good starting point for tackling similar problems. Happy coding 👩‍💻👨‍💻

## 📚 Learn more

- [Big O Notation](https://www.bigocheatsheet.com/)
- [JavaScript Arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [JavaScript Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
- [JavaScript Control Flow](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)

Remember, practice is the key 💪. Happy coding 👩‍💻👨‍💻

































