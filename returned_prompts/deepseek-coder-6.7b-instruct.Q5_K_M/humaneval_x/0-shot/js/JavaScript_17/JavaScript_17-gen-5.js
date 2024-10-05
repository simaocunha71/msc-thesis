  let beats = []
  let music = music_string.split(' ')

  for (let i = 0; i < music.length; i++) {
    switch(music[i]) {
      case 'o':
        beats.push(4)
        break
      case 'o|':
        beats.push(2)
        break
      case '.|':
        beats.push(1)
        break
    }
  }

  return beats
}

console.log(parseMusic('o o| .| o| o| .| .| .| .| o o')) // [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This function works by splitting the input string into an array of notes, then looping through that array. If a note matches one of the special cases, the corresponding number of beats is added to the `beats` array. Finally, the array of beats is returned.

Please note that this function assumes that the input string is correctly formatted and does not contain any errors. It may not behave correctly if given an improperly formatted string.

I hope this helps. Please let me know if you have any questions.

---

