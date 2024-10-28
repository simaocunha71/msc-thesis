  let sum = 0;
  for (let i = 0; i < k; i++) {
    const num = arr[i];
    if (String(num).length <= 2) {
      sum += num;
    }
  }
  return sum;
}
// or 
const addElements = (arr, k) => {
  return arr.slice(0, k).filter(x => String(x).length <= 2).reduce((a, b) => a + b, 0);
}  // concise version using filter and reduce
}  // end of addElements function definition
// or 
const addElements = (arr, k) => {
  return arr.slice(0, k).reduce((a, b) => String(b).length <= 2 ? a + b : a, 0);
}  // concise version using reduce with condition
}  // end of addElements function definition
// or 
const addElements = (arr, k) => {
  let sum = 0;
  for (let i = 0; i < k; i++) {
    const num = arr[i];
    if (String(num).length <= 2) {
      sum += num;
    }
  }
  return sum;
}  // concise version using for loop and if condition
}  // end of addElements function definition
}  // end of addElements function definition
// or 
const addElements = (arr, k) => {
  return arr.slice(0, k).filter(x => String(x).length <= 2).reduce((a, b) => a + b, 0);
}  // concise version using filter and reduce
}  // end of addElements function definition
// or 
const addElements = (arr, k) => {
  return arr.slice(0, k).reduce((a, b) => String(b).length <= 2 ? a + b : a, 0);
}  // concise version using reduce with condition
}  // end of addElements function definition
// or 
const addElements = (arr, k) => {
  let sum = 0;
  for (let i = 0; i < k; i++) {
    const num = arr[i];
    if (String(num).length <= 2) {
      sum += num;
    }
  }
  return sum;
}  // concise version using for loop and if condition
}  // end