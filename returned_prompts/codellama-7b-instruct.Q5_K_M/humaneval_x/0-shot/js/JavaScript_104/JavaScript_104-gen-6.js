
function uniqueDigits(x){

  let y = [];
  for (let i = 0; i < x.length; i++){
    if (x[i] % 2 !== 0){
      y.push(x[i]);
    }
  }
  y.sort(function(a, b){return a-b});
  return y;
}

