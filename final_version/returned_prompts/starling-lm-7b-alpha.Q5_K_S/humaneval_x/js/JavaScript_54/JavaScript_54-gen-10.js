  const s0_list = s0.split('');
  const s1_list = s1.split('');

  if (s0_list.length != s1_list.length) {
    return false;
  }

  s0_list.sort();
  s1_list.sort();

  for (let i = 0; i < s0_list.length; i++) {
    if (s0_list[i] != s1_list[i]) {
      return false;
    }
  }

  return true;
}



