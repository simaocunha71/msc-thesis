      if(token === tokens2[j]) {
        values += token + ' ';
        tokens1.splice(i, 1);
        tokens2.splice(j, 1);
        i--;
        continue outer;
      }
    }
  }
  return values;
}

