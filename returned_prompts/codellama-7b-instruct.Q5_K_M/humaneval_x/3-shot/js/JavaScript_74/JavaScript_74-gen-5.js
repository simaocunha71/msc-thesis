  let sum_lst1 = lst1.reduce((acc, curr) => acc + curr.length, 0);
  let sum_lst2 = lst2.reduce((acc, curr) => acc + curr.length, 0);

  if (sum_lst1 > sum_lst2) return lst2;
  else return lst1;
}



