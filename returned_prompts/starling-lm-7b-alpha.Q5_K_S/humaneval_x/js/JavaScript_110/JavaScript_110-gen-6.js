  const evens_in_first = lst1.filter(num => num % 2 === 0);
  const odds_in_first = lst1.filter(num => num % 2 !== 0);
  const evens_in_second = lst2.filter(num => num % 2 === 0);
  const odds_in_second = lst2.filter(num => num % 2 !== 0);

  if (odds_in_first.length === 0 && evens_in_second.length >= evens_in_first.length) {
    return "YES";
  }

  return "NO";
}



