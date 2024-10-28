  return l.map((element, index) => {
    if (index % 3 == 0) {
      return element;
    } else {
      return l[index];
    }
  }).sort();
}



