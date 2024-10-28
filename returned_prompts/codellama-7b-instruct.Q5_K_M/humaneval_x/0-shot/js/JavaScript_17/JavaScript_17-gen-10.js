const parseMusic = music_string =>
  music_string.replace(/\./g, '').split('|').map(s => s.length === 1 ? 1 : 2)
