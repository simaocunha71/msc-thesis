      if(token === tokens2[j]) {
        values += tokens2.slice(j).join(' ');
        continue outer;
      }
    }
  }
  values += tokens2.join(' ');
  return values;
}

