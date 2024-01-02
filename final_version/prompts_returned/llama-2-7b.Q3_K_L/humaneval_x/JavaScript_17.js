/* Input to this function is a string representing musical notes in a special ASCII format.
  Your task is to parse this string and return list of integers corresponding to how many beats does each
  not last.

  Here is a legend:
  'o' - whole note, lasts four beats
  'o|' - half note, lasts two beats
  '.|' - quater note, lasts one beat

  >>> parseMusic('o o| .| o| o| .| .| .| .| o o')
  [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
  */
const parseMusic = (music_string) => {
  let parsed_music = [];
  const notes_per_beat_lengths = {};
  for(let i=0; i< music_string.length; i++){
    if((i%2 == 0 && i != 0 ) || (i %3 == 1)){
      let currentNoteLength = parseInt((music_string[i] === 'o' ? 4 : 2),10); //we assume that o means whole note and .| quarter
      if(notes_per_beat_lengths[currentNoteLength]){
        parsed_music.push(notes_per_beat_lengths[currentNoteLength] + currentNoteLength)
        notes_per_beat_lengths[currentNoteLength] = 0;
      }else{
        notes_per_beat_lengths[currentNoteLength] = currentNoteLength
      }
    }
  }
  return parsed_music
}
