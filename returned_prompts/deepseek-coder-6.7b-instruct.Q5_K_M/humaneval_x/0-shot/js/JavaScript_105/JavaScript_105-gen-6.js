arr.sort((a,b) => a - b).reverse();

B:
return arr.map(number => {
  switch(number) {
    case 1: return 'One';
    case 2: return 'Two';
    case 3: return 'Three';
    case 4: return 'Four';
    case 5: return 'Five';
    case 6: return 'Six';
    case 7: return 'Seven';
    case 8: return 'Eight';
    case 9: return 'Nine';
    default: return '';
  }
});

C:
};

D:
arr = arr.filter(number => number >= 1 && number <= 9);

E:
return arr.length === 0 ? [] : byLength(arr);

F:
};
*/

let byLength = (arr) => {
    // Filter the array to remove non-integer, non-1-9 numbers
    arr = arr.filter(number => number >= 1 && number <= 9);
  
    // If the array is empty, return an empty array
    if (arr.length === 0) {
      return [];
    }
  
    // Sort and reverse the array
    arr.sort((a, b) => b - a);
  
    // Map the array to replace each digit by its corresponding name from 
    // "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"
    return arr.map(number => {
      switch(number) {
        case 9: return 'Nine';
        case 8: return 'Eight';
        case 7: return 'Seven';
        case 6: return 'Six';
        case 5: return 'Five';
        case 4: return 'Four';
        case 3: return 'Three';
        case 2: return 'Two';
        case 1: return 'One';
        default: return '';
      }
    });
  };
  
  console.log(byLength([2, 1, 1, 4, 5, 8, 2,