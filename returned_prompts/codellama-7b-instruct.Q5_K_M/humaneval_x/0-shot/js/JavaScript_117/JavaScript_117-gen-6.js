
  function selectWords(str, cnt) {
    const words = str.split(" ");
    return words.filter(word => word.replace(/[aeiou]/g, "").length === cnt);
  }
  const selectWords = (str, cnt) => {
    return str.split(" ").filter(word => word.replace(/[aeiou]/g, "").length === cnt);
  }
  const selectWords = (s, n) => s.split(" ").filter(w => w.replace(/[aeiou]/g, "").length === n);
  const selectWords = (s, n) => s.split(" ").filter(w => /[aeiou]/.test(w.replace(/[aeiou]/g, ""))).length === n;
  const selectWords = (s, n) => s.split(" ").filter(w => w.length - w.replace(/[aeiou]/g, "").length === n);
  const selectWords = (s, n) => s.split(" ").filter(w => w.match(new RegExp("[^aeiou]", 'g')).length === n);
  const selectWords = (s, n) => s.split(" ").filter(w => w.replace(/[aeiou]/g, "").length === n);
  const selectWords = (s, n) => s.split(" ").filter(w => w.length - w.replace(/[aeiou]/g, "").length === n);
  const selectWords = (s, n) => s.split(" ").filter(w => w.match(new RegExp("[^aeiou]", 'g')).length === n);

B:
  const selectWords = (str, cnt) => {
    let words = [];
    str.split(" ").forEach(word => {
      if (word.replace(/[aeiou]/g, "").length === cnt) {
        words.push(word);
      }
    });
    return words;
  }
  const selectWords = (s, n) => {
    let words =