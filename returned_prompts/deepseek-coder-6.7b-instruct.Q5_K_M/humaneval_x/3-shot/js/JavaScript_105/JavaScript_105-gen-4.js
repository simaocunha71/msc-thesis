  const words = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'];
  return arr.filter(el => el >= 1 && el <= 9)
             .sort((a, b) => b - a)
             .map(el => words[el]);
}



