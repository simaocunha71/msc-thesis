  let smallest = null;
  let nextSmallest = null;
  for  (let i = 0; i < lst.length; i++)  {
    if  (smallest === null || lst[i] < smallest)  {
      nextSmallest = smallest;
      smallest = lst[i];
    }  else if  (nextSmallest === null || lst[i] < nextSmallest && lst[i] !== smallest)  {
      nextSmallest = lst[i];
    }
  }
  return nextSmallest;
}



