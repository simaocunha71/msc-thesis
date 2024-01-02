/*
  Write a function that accepts two lists of strings and returns the list that has
  total number of chars in the all strings of the list less than the other list.

  if the two lists have the same number of chars, return the first list.

  Examples
  totalMatch([], []) ➞ []
  totalMatch(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
  totalMatch(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
  totalMatch(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
  totalMatch(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
  */
const totalMatch = (lst1, lst2) => {
  let length = lst1.length;
  if(length == lst2.length) return lst1[0];
  else{
    for(let index = 0; index < length; index++){
      if(lst1[index] > lst2[index]){
        return lst1;
      }else{
        if(lst1[index] === lst2[index]){
          console.log("same");
          return lst1;
        }else{
          //if two list have same number of strings, return the first element from both lists
          let temp = totalMatch([lst1[index], ...lst2], [...lst1, lst2[index]]);
          console.log(temp)
          return temp;
        }
      }
    }
  }
}
