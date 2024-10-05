  let lst1_odd = lst1.filter((x) => x % 2 != 0);
  let lst2_even = lst2.filter((x) => x % 2 == 0);

  if (lst1_odd.length <= lst2_even.length) {
    return "YES";
  } else {
    return "NO";
  }
}