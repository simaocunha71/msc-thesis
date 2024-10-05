  for (const num of lst1) {
    if (num % 2 !== 0) {
      let found = false;
      for (const num2 of lst2) {
        if (num2 % 2 === 0) {
          lst1[lst1.indexOf(num)] = num2;
          lst2[lst2.indexOf(num2)] = num;
          found = true;
          break;
        }
      }
      if (!found) {
        return "NO";
      }
    }
  }
  return "YES";
}