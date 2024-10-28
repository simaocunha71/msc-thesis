  let count = 0;
  let arr = [];
  for(let i=1; i<=n; i++) {
      arr.push(i*i - i + 1);
  }
  for(let i=0; i<n-2; i++) {
      for(let j=i+1; j<n-1; j++) {
          for(let k=j+1; k<n; k++) {
              if((arr[i] + arr[j] + arr[k]) % 3 === 0) count++;
          }
      }
  }
  return count;
}




