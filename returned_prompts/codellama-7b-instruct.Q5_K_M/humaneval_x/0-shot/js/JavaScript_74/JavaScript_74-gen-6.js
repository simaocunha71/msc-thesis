function totalMatch(lst1, lst2){
	let total1 = 0;
	let total2 = 0;
	for (let i = 0; i < lst1.length; i++){
		total1 += lst1[i].length;
	}
	for (let j = 0; j < lst2.length; j++){
		total2 += lst2[j].length;
	}
	if (total1 < total2){
		return lst1;
	}
	else if (total1 > total2){
		return lst2;
	}
	else if (total1 === total2){
		return lst1;
	}
}
