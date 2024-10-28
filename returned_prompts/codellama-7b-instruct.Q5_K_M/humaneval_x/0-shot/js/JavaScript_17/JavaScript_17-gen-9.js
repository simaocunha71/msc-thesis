const parseMusic = (music_string) => {
  return music_string.split('').map((note) => {
    switch (note) {
      case 'o':
        return 4;
      case 'o|':
        return 2;
      case '.|':
        return 1;
      default:
        return 0;
    }
  });
};

B:
const parseMusic = (music_string) => {
  return music_string.split('').map((note) => {
    switch (note) {
      case 'o':
        return 4;
      case '|':
        return 2;
      default:
        return 1;
    }
  });
};

C:
const parseMusic = (music_string) => {
  return music_string.split('').map((note) => {
    switch (note) {
      case 'o':
        return 4;
      case 'o':
        return 2;
      default:
        return 1;
    }
  });
};

D:
const parseMusic = (music_string) => {
  return music_string.split('').map((note) => {
    switch (note) {
      case 'o':
        return 4;
      case '|':
        return 2;
      default:
        return 1;
    }
  });
};

E:
const parseMusic = (music_string) => {
  return music_string.split('').map((note) => {
    switch (note) {
      case 'o':
        return 4;
      case 'o':
        return 2;
      case '|':
        return 1;
      default:
        return 0;
    }
  });
};

F:
const parseMusic = (music_string) => {
  return music_string.split('').map((note) => {
    switch (note) {
      case 'o':
        return 4;
      case '|':
        return 2;
      case '|':
        return 1;
      default:
        return 0;
   