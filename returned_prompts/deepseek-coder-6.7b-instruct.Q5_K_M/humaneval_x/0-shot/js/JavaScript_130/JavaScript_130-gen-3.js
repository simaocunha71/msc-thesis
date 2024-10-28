  let arr = [1, 3, 2];
  for(let i = 3; i <= n; i++){
    if(i % 2 === 0){
      arr[i] = 1 + i / 2;
    }else{
      arr[i] = arr[i - 1] + arr[i - 2] + arr[i + 1];
    }
  }
  return arr;
}

console.log(tri(3));

But this solution is not correct because at the line arr[i] = arr[i - 1] + arr[i - 2] + arr[i + 1]; it will throw an error because arr[i + 1] is not defined in the array.

