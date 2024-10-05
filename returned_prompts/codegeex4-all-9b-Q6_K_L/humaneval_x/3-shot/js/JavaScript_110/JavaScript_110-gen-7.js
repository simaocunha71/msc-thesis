  var even_count = lst1.filter((x) => x % 2 == 0).length;
  var odd_count = lst2.filter((x) => x % 2 == 1).length;

  return (even_count + odd_count) >= lst1.length;
}