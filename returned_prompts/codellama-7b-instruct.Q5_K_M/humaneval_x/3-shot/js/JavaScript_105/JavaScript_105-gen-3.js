  const names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'];
  const names_dict = {};
  for (let i = 0; i < names.length; i++) {
    names_dict[names[i]] = i;
  }

  const sorted = arr.filter(x => x >= 1 && x <= 9).sort((a, b) => a - b);

  const sorted_names = sorted.map(x => names[x - 1]);

  return sorted_names;
}



