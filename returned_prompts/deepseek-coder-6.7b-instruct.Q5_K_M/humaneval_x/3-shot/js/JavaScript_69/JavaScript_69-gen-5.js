  let count_map  = {};
  for  (let num of lst)  {
    if  (count_map[num])  {
      count_map[num]++;
     } else  {
      count_map[num] = 1;
     }
  }
  for  (let i = lst.length; i > 0; i--)  {
    if  (count_map[i])  {
      if  (count_map[i] >= i)  {
        return i;
       }
     }
  }
  return -1;
}



