  var num1 = parseInt(x.split('/')[0]) * parseInt(n.split('/')[1]);
  var den1 = parseInt(x.split('/')[1]) * parseInt(n.split('/')[0]);
  var num2 = parseInt(x.split('/')[0]) * parseInt(n.split('/')[0]);
  var den2 = parseInt(x.split('/')[1]) * parseInt(n.split('/')[1]);
  return num1 === num2 && den1 === den2;
}
// or
const simplify = (x, n) => {
  var a = parseInt(x.split('/')[0]);
  var b = parseInt(x.split('/')[1]);
  var c = parseInt(n.split('/')[0]);
  var d = parseInt(n.split('/')[1]);
  return a * d === b * c;
}