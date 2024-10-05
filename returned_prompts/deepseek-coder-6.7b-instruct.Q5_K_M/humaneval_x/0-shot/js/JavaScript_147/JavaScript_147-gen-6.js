let arr = new Array(n);

  for(let i = 1; i <= n; i++){
    arr[i-1] = i*i - i + 1;
  }

  let count = 0;

  for(let i = 0; i < n; i++){
    for(let j = i+1; j < n; j++){
      for(let k = j+1; k < n; k++){
        if((arr[i] + arr[j] + arr[k]) % 3 === 0) count++;
      }
    }
  }

  return count;
};

//Time complexity: O(n^3)
//Space complexity: O(n)

//Example:
console.log(getMaxTriples(5)); //Output: 1

/*
  You are given a positive integer n. You have to create an integer array a of length n.
      For each i  (1 ≤ i ≤ n), the value of a[i]  is i  * i  - i + 1.
      Return the number of triples  (a[i], a[j], a[k]) of a where i ≤ j ≤ k, 
  and a[i] ⊕ a[j] ⊕