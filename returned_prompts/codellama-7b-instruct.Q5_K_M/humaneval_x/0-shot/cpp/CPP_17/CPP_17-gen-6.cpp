  /*
  What if we just count the number of "o"s?
  */
  int n_whole_notes = 0;
  int n_half_notes = 0;
  int n_quater_notes = 0;
  for(int i=0; i<music_string.size(); i++){
    if(music_string[i] == 'o'){
      n_whole_notes++;
      n_half_notes++;
    }
    if(music_string[i] == '|'){
      n_half_notes++;
      n_quater_notes++;
    }
  }

  vector<int> beats;
  for(int i=0; i<n_whole_notes; i++) beats.push_back(4);
  for(int i=0; i<n_half_notes; i++) beats.push_back(2);
  for(int i=0; i<n_quater_notes; i++) beats.push_back(1);
  return beats;
}


int main(){
  vector<int> beats = parse_music("o o| .| o| o| .| .| .| .| o o");
  for(int i=0; i<beats.size(); i++) printf("%d ", beats[i]);
  printf("\n");
  return 0;
}
