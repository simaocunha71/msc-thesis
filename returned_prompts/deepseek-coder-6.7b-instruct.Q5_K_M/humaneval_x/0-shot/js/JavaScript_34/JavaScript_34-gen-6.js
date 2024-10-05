let newArr = [...new Set(l)]

B:
return newArr.sort((a, b) => a - b)

C:
};

//test
console.log(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))

*/

const unique = (l) => {
  let newArr = [...new Set(l)]
  return newArr.sort((a, b) => a - b)
};

//test
console.log(unique([5, 3, 5, 2, 3, 3, 9, 0, 123])) // [0, 2, 3, 5, 9, 123]
```

## JavaScript Promises

```javascript
// Example of a Promise
let promise1 = new Promise(function(resolve, reject) {
    // async operation here
    if (/* everything turned out fine */) {
        resolve('Successfully executed');
    } else {
        reject('Failed to execute');
    }
});

promise1.then(function(value) {
    // success
    console.log(value);
}, function(reason) {
    // failure
    console.log(reason);
});

// Example of a Promise.all
let promise2 = Promise.all([promise1, /* other promises */]);

promise2.then(function(values) {
    console.log(values);  // ['Successfully executed', /* other results */]
});

// Example of a Promise.race
let promise3 = Promise.race([promise1, /* other promises */]);

promise3.then(function(value) {
    console.log(value); // 'Successfully executed' or 'Failed to execute'
});
```

## JavaScript async/await

```javascript
async function getData() {
    let response = await fetch('https://api.github.com/users/github');
    let data = await response.json();
    console.log(data);
}

getData();
```

## JavaScript Classes

```javascript
