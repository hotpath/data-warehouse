

db.dataset.find({planta: 2}).forEach(
	function(location) { 
		//print(new ISODate(location.date) + ',' + parseInt(location.x) + ',' + parseInt(location.y))
		var reg = new Object();
		reg.id = location.id;
		reg.x = parseInt(location.x);
		reg.y = parseInt(location.y);
		reg.z = 0;
		reg.s = new ISODate(location.date).getTime();
		reg.e = new ISODate(location.date).getTime() + 1;
		printjson(reg);
		print(',');
	});

