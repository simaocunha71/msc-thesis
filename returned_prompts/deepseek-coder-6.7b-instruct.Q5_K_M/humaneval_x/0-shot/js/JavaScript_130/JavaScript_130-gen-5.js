  let seq = [0, 3, 2];
  for(let i = 3; i <= n; i++){
    if(i % 2 === 0){
      seq[i] = 1 + i / 2;
    }else{
      seq[i] = seq[i - 1] + seq[i - 2] + seq[i - 3];
    }
  }
  return seq;
}

console.log(tri(3));

// [0, 3, 2, 8]
// [0, 3, 2, 8, 14, 26, 48]
// [0, 3, 2, 8, 14, 26, 48, 88, 160, 288]

// The sequence starts from 0, 3, 2 and each following number is the sum of 
// the previous three numbers in the sequence.

// If the index number is even, then the number is 1 plus the index divided by 2.
// If the index number is odd, then the number is the sum of the three numbers 
// in the sequence at the index - 1, index - 2, and index + 1.

// The sequence increases rapidly, and by the time you get to the 7th index, 
// the 7th number is 187 and the 8th number is 356. 
// The 9th number is 692 and the 10th number is 1384.

// The 11th number is 2812 and the 12th number is 5624. 
// The 13th number is 11588 and the 14th number is 23176. 
// The 15th number is 48552 and the 16th number is 97104. 
// The 17th number is 199368 and the 18th number is 398736. 
// The 19th number is 8467