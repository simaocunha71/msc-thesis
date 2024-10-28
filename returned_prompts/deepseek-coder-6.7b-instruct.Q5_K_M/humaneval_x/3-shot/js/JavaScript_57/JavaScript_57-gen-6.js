  return (l.slice(0).sort((a, b) => a - b).toString() === l.toString()) ||
         (l.slice(0).sort((a, b) => b - a).toString() === l.toString());
}



