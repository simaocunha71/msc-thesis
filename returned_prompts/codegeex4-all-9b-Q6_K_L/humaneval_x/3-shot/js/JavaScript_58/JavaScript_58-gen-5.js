  var commonElements = [];
  l1.forEach(function (element) {
    if (l2.includes(element) && !commonElements.includes(element)) {
      commonElements.push(element);
    }
  });
  return commonElements.sort((a, b) => a - b);
}



