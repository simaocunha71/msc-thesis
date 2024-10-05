  return s.split(' ')
          .map(word => word.split('')
                           .sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0))
                           .join(''))
          .join(' ');
}



