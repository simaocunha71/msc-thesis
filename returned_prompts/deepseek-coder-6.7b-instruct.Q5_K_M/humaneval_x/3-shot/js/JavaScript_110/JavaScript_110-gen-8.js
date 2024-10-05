  let odd1 = lst1.filter(x => x % 2 !== 0);
  let even2 = lst2.filter(x => x % 2 === 0);

  return odd1.length <= even2.length ? "YES" : "NO";
}



