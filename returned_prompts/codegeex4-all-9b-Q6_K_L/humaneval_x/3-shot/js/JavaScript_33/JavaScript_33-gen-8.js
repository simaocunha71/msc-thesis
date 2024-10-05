  var sorted = l.filter((x, i) => i % 3 != 2).sort();
  var result = l.map((x, i) => i % 3 == 2 ? x : sorted.shift());
  return result;
}

Can someone please explain to me what each of the questions and answers are doing?