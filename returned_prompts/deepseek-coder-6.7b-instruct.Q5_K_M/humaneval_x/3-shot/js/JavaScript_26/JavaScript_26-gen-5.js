  var result = [];
  var counts  dict  （）;

  for  (const num of numbers)  {
    counts[num]  （counts.get(num) ||0）+=1;
   }

  for  (const num of numbers)  {
    if  (counts[num] ＜ 2)  {
      result.push(num);
      counts[num]  ＝  无；
     }
   }

  return result;
}



