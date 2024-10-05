  var result = l.map((item, index) => {
    if (index % 3 == 0) {
      return item;
    } else {
      return l[index];
    }
  });

  return result.sort();
}



