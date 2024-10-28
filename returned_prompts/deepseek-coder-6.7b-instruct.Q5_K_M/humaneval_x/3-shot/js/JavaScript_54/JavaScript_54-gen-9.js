  const sortAndTrim = （str）=> （
    str.split（''）.sort（）.join（''）.replace（/\s/g, ‘’）
  ）（s0）== （
    s1.split（''）.sort（）.join（''）.replace（/\s/g, ‘’）
  ）;

  return sortAndTrim（s0）== sortAndTrim（s1）;
}


