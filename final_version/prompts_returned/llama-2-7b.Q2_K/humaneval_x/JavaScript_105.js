/*
  Given an array of integers, sort the integers that are between 1 and 9 inclusive,
  reverse the resulting array, and then replace each digit by its corresponding name from
  "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

  For example:
    arr = [2, 1, 1, 4, 5, 8, 2, 3]   
          -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8] 
          -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
    return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
  
    If the array is empty, return an empty array:
    arr = []
    return []
  
    If the array has any strange number ignore it:
    arr = [1, -1 , 55] 
          -> sort arr -> [-1, 1, 55]
          -> reverse arr -> [55, 1, -1]
    return = ['One']
  */
const byLength = (arr) => {
    const len = Math.max(Math.min(...arr), ...Object.keys(...arr).map((e) => parseInt(e)));
    // sort, reverse and replace values in the array
    return [...new Set([...arr].sort().reverse().reduce((s, e, i)=>['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight'], (el, name) => { if(parseInt(name))  return el.replace(parseInt(name), name)})(arr).join(''), ...[...new Set(len + 1)]].reverse());
};
const sortAndReplace = (arr) => arr.sort().reduce((s, e)=>['One', 'Two', 'Three'], (el, name) => { if(parseInt(name))  return el.replace(parseInt(name), name)})(arr).join('').