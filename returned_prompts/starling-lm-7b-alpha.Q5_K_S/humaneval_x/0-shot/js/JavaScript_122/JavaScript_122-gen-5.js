
const firstKElements = arr.slice(0, k);
let sum = 0;

for (let i = 0; i < k; i++) {
  if (firstKElements[i].toString().length <= 2) {
    sum += firstKElements[i];
  }
}

return sum;

};

console.log(addElements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4));

B:

const arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9];
const k = 4;

let sum = 0;

for (let i = 0; i < k; i++) {
  if (arr[i].toString().length <= 2) {
    sum += arr[i];
  }
}

console.log(sum);

C:

function addElements(arr, k) {
  let sum = 0;

  for (let i = 0; i < k; i++) {
    if (arr[i].toString().length <= 2) {
      sum += arr[i];
    }
  }

  return sum;
}

console.log(addElements(arr, k));

D:

function addElements(arr, k) {
  var sum = 0;
  for (var i = 0; i < k; i++) {
    if (arr[i].toString().length <= 2) {
      sum += arr[i];
    }
  }
  return sum;
}

console.log(addElements(arr, k));

E:

function addElements(arr, k) {
  var sum = 0;
  for (var i = 0; i < k; i++) {
    if (arr[i].toString().length <= 2) {
      sum += arr[i];
    }
  }
  return sum;
}

console.log(addElements(arr, k));

F:

