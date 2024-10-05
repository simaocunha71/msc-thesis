  var a = s.indexOf('apples');
  var o = s.indexOf('oranges');
  var m = n - (parseInt(s.slice(0, a)) + parseInt(s.slice(o + 7)));
  return m;
}



