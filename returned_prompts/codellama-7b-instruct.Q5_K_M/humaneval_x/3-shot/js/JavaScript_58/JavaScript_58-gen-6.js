  var common_elements = []

  for (const e1 of l1) {
    for (const e2 of l2) {
      if (e1 == e2) {
        if (!common_elements.includes(e1)) {
          common_elements.push(e1);
        }
      }
    }
  }

  return common_elements.sort((a, b) => a - b);
}



