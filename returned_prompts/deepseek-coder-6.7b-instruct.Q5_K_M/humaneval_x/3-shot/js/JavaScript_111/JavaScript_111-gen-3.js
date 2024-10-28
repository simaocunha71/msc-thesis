  let count = {};
  let words = test.split(' ');
  let max = 0;
  let result = {};

  for(let word of words){
    if(count[word]){
      count[word]++;
    }else{
      count[word] = 1;
    }

    if(count[word] > max){
      max = count[word];
      result = {[word]: max};
    }else if(count[word] == max){
      result[word] = max;
    }
  }

  return result;
}



