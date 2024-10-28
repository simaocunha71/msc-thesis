/*
  Solution:
  We will iterate through the list and see if we can find an even number in lst2
  that we can exchange with an odd number in lst1.
  If we are able to find at least one even number in lst2 to exchange with
  at least one odd number in lst1, we will return "YES".
  If we are unable to find an even number in lst2 to exchange with an odd
  number in lst1, we will return "NO".
  */
  for(let i = 0; i < lst2.length; i++){
    if(lst2[i] % 2 === 0 && lst1.includes(lst2[i])){
      for(let j = 0; j < lst1.length; j++){
        if(lst1[j] % 2 !== 0 && lst2.includes(lst1[j])){
          [lst1[j], lst2[i]] = [lst2[i], lst1[j]]
        }
      }
    }
  }
  return lst1.every(num => num % 2 === 0) ? "YES" : "NO"
}

