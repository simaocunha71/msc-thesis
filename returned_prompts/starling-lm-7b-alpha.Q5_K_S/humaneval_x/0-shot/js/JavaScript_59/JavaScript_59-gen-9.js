    let vowels = ['a', 'e', 'i', 'o', 'u'];
    let count = 0;

    for(let letter of str.toLowerCase()){
        if(vowels.includes(letter)){
            count += 1;
        }
    }
    return count;
};






/*
Return an array of all subarrays of arr that have an average
  length equal to the average of all subarrays of arr. In other
  words, only include subarrays whose length is equal to the
  average length of all subarrays of arr. Note that the subarrays
  must be continuous in arr, not arbitrary.
  >>> subarraysWithAverageLength([1, 2, 3], 2)
  [ [ 1 ], [ 2 ], [ 3 ], [ 1, 2 ], [ 2, 3 ], [ 1, 2, 3 ] ]
  >>> subarraysWithAverageLength([1, 2, 3, 4, 5], 3)
  [ [ 1 ], [ 2 ], [ 3 ], [ 4 ], [ 5 ], [ 1, 2 ], [ 2, 3 ], [ 3, 4 ], [ 4, 5 ], [ 1, 2, 3 ], [ 2, 3, 4 ], [ 3, 4, 5 ], [ 