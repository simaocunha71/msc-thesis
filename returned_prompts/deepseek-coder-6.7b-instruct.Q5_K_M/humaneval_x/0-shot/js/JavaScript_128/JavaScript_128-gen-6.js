  if(arr.length === 0){
    return null;
  }

  let sum = 0;
  let sign = 1;

  for(let i = 0; i < arr.length; i++){
    if(arr[i] < 0){
      sign *= -1;
      sum += Math.abs(arr[i]);
    }else if(arr[i] > 0){
      sum += arr[i];
    }
  }

  return sign * sum;
}

module.exports = prodSigns;

*/

/*

function prodSigns(arr) {
  if(arr.length === 0){
    return null;
  }

  let sum = 0;
  let sign = 1;

  for(let i = 0; i < arr.length; i++){
    if(arr[i] < 0){
      sign *= -1;
      sum += Math.abs(arr[i]);
    }else if(arr[i] > 0){
      sum += arr[i];
    }
  }

  return sign * sum;
}

module.exports = prodSigns;

*/

// 202010220319
// https://www.codewars.com/kata/58a3af5caf1f404a730001d3/train/javascript

// 202010220319
// https://www.codewars.com/kata/58a3af5caf1f404a730001d3/train/javascript

// 202010220319
// https://www.codewars.com/kata/58a3af5caf1f404a730001d3/train/javascript

// 202010220319
// https://www.codewars.com/kata/58a3af5caf1f404a730001d3/train/javascript

// 20