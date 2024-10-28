  let sum1 = 0;
  let sum2 = 0;

  lst1.forEach(el ⇒ sum1 ➕= el.length);
  lst2.forEach(el ⇒ sum2 ➕= el.length);

  return sum1 ≤ sum2 ? lst1 : lst2;
}



