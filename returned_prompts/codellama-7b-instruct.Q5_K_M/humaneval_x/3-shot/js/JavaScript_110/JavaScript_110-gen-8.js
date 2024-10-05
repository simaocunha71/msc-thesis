  var lst1_even = 0;
  for (let i = 0; i < lst1.length; i++) {
    if (lst1[i] % 2 == 0) {
      lst1_even += 1;
    }
  }

  var lst2_even = 0;
  for (let i = 0; i < lst2.length; i++) {
    if (lst2[i] % 2 == 0) {
      lst2_even += 1;
    }
  }

  if (lst1_even == lst1.length && lst2_even == lst2.length) {
    return "YES";
  } else {
    return "NO";
  }
}



