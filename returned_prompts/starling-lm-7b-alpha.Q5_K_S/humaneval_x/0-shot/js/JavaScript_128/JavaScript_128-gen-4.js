  let result = 0;
  let sign = 1;
  if(arr.length === 0){
    return null;
  }
  for(let i = 0; i < arr.length; i++){
    if(arr[i] > 0){
      result += arr[i];
      sign *= 1;
    }else if(arr[i] < 0){
      result += arr[i] * -1;
      sign *= -1;
    }else if(arr[i] === 0){
      result += 0;
      sign *= 0;
    }
  }
  if(sign === 0){
    return 0;
  }else{
    return result * sign;
  }

};


/*
  You are given an array arr of integers and you need to return
  the minimum cost of buying and selling the stock,
  represented by arr[0] to arr[n-1]. You can complete at most two
  transactions. You cannot sell more than twice.

  Example:
  >>> minCost( [3, 1, 4, 2, 5, 3, 5, 6] ) == 5
  >>> minCost( [7, 1, 5, 3, 6, 4] ) == 7
  >>> minCost( [1] ) == 0
  >>> minCost( [1, 2] ) == 0
  >>> minCost([]) == null
  >>> minCost([7]) == 0

  Hint:
  Consider the case where you can only sell once and only buy once.
  Consider the case where you can only sell once and you can only buy once or twice.
  Consider the case where you can only sell twice and you can only buy once or twice.
 */

const minCost = (arr) => {

  if(arr.length === 0){
    return 0;
  }
  let minCost = Infinity;
  let minCostFirst = Infinity;
  let minCostSecond = Infinity;
  let minCostThird = Infinity;
  let minCostFourth = Infinity;
  let minCost