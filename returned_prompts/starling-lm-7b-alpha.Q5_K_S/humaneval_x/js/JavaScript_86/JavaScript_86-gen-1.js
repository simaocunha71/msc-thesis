  const chars = s.split('');
  const sorted_chars = chars.sort((a,b) => a.charCodeAt(0) - b.charCodeAt(0));
  const result = sorted_chars.join('');
  return result;
};



