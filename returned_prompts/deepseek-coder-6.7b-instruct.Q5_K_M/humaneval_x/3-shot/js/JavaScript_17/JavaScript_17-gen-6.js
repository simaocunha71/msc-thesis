  return music_string.split(' ').map(x => {
    switch(x) {
      case 'o': return 4;
      case 'o|': return 2;
      case '.|': return 1;
      default: return 0;
    }
  });
}



