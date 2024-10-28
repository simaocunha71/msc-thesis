  let [_, apples, oranges] = s.match(/\d+/g);
  apples = parseInt(apples);
  oranges = parseInt(oranges);
  return n - apples - oranges;

};

console.log(fruitDistribution("5 apples and 6 oranges", 19)); // 8
console.log(fruitDistribution("0 apples and 1 oranges", 3)); // 2
console.log(fruitDistribution("2 apples and 3 oranges", 100)); // 95
console.log(fruitDistribution("100 apples and 1 oranges", 120)); // 19




// the solution is very simple it uses the regex to find the numbers in the string and then subtracts the numbers of apples and oranges from the total number of fruits to get the number of mangoes.
// the parseInt function is used to convert the string numbers to integers.
// finally the result is returned.

// This solution works because the problem statement clearly states that the number of fruits is given as an integer and the number of apples and oranges are also given as integers in the string.

// The time complexity of this solution is O(1) because it always does the same amount of work regardless of the size of the input.

// The space complexity is also O(1) because it only uses a constant amount of space to store the input and the result.

// It's important to note that this solution assumes that the input will always be in the correct format as stated in the problem statement. If this is not the case, additional error checking would be needed.
</code>

</body>
</html>























































































































