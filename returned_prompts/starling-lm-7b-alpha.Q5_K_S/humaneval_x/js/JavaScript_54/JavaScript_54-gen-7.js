  let s0_list = s0.split('');
  let s1_list = s1.split('');

  s0_list.sort();
  s1_list.sort();

  return s0_list.length == s1_list.length && s0_list.join('') == s1_list.join('');
}



