  let class_name_len = class_name.length;
  let strongest_extension = '';
  let strength = -1;

  for (const ext of extensions) {
    let ext_len = ext.length;
    let cap_cnt = 0;
    let sm_cnt = 0;

    for (const ch of ext) {
      if (ch == ch.toLowerCase()) {
        sm_cnt += 1;
      } else if (ch == ch.toUpperCase()) {
        cap_cnt += 1;
      }
    }

    let strength_val = cap_cnt - sm_cnt;

    if ((strength_val >= strength) && (ext_len <= class_name_len)) {
      strength = strength_val;
      strongest_extension = ext;
    }
  }

  return class_name + '.' + strongest_extension;
}



