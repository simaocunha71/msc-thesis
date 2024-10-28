  let result = arr.sort((a, b) => a - b);
  let reverse = result.reverse();
  let names = reverse.map(item => {
    if(item >= 1 && item <= 9) {
      return switch(item) {
        case 1: "One";
        case 2: "Two";
        case 3: "Three";
        case 4: "Four";
        case 5: "Five";
        case 6: "Six";
        case 7: "Seven";
        case 8: "Eight";
        case 9: "Nine";
      };
    } else {
      return " ";
    };
  });
  return names;
}
