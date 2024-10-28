      if(token == tokens2[j]) continue outer;
    }
    values += token + ' ';
  }

  for(var k = 0; k < tokens2.length; k++) {
    var token = tokens2[k];
    for(var l = 0; l < tokens1.length; l++) {
      if(token == tokens1[l]) continue outer;
    }
    values += token + ' ';
  }

  return values;
}

