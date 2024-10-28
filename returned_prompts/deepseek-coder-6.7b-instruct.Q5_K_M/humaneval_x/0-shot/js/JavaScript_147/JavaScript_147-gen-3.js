  let arr = [];
  for(let i = 1; i <= n; i++){
    arr.push(i * i - i + 1);
  }

  let count = 0;
  for(let i = 0; i < n; i++){
    for(let j = i + 1; j < n; j++){
      for(let k = j + 1; k < n; k++){
        if((arr[i] + arr[j] + arr[k]) % 3 === 0){
          count++;
        }
      }
    }
  }
  return count;
}

console.log(getMaxTriples(5)); // 1

*/

The above problem can be solved by using the basic concept of the combination.

The question wants to find the number of triples that can be formed from the array `a`. Here, `a` is an array of the form `a[i] = i * i - i + 1`.

The array `a` will be of the form `a[i] = n * n - n + 1` for `n = 1 to n`. 

If we consider the array `a`, we can see that the array will be of the form `a[i] = n * (n - 1) + (n - 1) * (n - 2) / 2`.

The question is asking for the triples where the sum of the elements of the triples is a multiple of 3. 

If we consider the array `a`, we can see that the array will be of the form `a[i] = n * (n - 1) + (n - 1) * (n - 2) / 2`. 

The sum of the elements of the triples `(a[i], a[j], a[k])` will be `a[i] + a[j] + a[k] = n * n - n + 1 + n * (n - 1) / 2`.

If we consider the array `a`, we can see that the array will be of the form `a[i] = n * n - n + 1 + n * (n -