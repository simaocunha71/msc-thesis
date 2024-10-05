  function histogram(str){
  let arr = str.split(" ");
  let obj = {};
  let max = 0;
  for (let i = 0; i < arr.length; i++){
    if(obj[arr[i]]){
      obj[arr[i]]++;
    }
    else{
      obj[arr[i]] = 1;
    }
    if (obj[arr[i]] > max){
      max = obj[arr[i]];
    }
  }
  for (let key in obj){
    if (obj[key] === max){
      console.log(key)
      console.log(obj[key]);
    }
  }
}



