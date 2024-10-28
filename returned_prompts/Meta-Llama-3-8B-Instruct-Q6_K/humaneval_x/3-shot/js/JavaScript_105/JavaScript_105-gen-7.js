  let result = [];
  let numbers = arr.filter(num => num >= 1 && num <= 9);
  numbers.sort((a, b) => a - b).reverse();
  numbers.forEach(num => {
    switch (num) {
      case 1:
        result.push("One");
        break;
      case 2:
        result.push("Two");
        break;
      case 3:
        result.push("Three");
        break;
      case 4:
        result.push("Four");
        break;
      case 5:
        result.push("Five");
        break;
      case 6:
        result.push("Six");
        break;
      case 7:
        result.push("Seven");
        break;
      case 8:
        result.push("Eight");
        break;
      case 9:
        result.push("Nine");
        break;
    }
  });
  return result;
}