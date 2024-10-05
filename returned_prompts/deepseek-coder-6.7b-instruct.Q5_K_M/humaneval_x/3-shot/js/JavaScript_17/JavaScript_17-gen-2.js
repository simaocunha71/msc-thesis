  var notes = music_string.split(' ');
  var result = [];

  for  (const note of notes)  {
    switch  (note)  {
      case  'o':
        result.push(4);
        break;
      case  'o|':
        result.push(2);
        break;
      case  '.|':
        result.push(1);
        break;
     }
   }

  return result;
}



