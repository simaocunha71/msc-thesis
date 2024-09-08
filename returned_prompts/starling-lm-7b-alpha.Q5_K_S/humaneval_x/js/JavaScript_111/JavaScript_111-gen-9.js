  let result = {};
  let splitTest = test.split(' ');
  for (let i = 0; i < splitTest.length; i++) {
    if (result[splitTest[i]] == undefined) {
      result[splitTest[i]] = 1;
    } else {
      result[splitTest[i]] += 1;
    }
  }
  return result;
}



