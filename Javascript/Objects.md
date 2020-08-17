
# Javascript Notes

# Understanding Objects

Objects in JavaScript are dynamic, meaning that they can change at any point during code execution. Whereas class-based languages lock down objects based on a class definition, JavaScript objects have no such restrictions.

**Detecting Properties**
	
	var person1 = {
			name: "Nicholas", 
			sayName: function() {
				console.log(this.name); 
			}
	};
	
	console.log("sayName" in person1); // true

**Removing Properties**

    var person1 = { 
	    name: "Nicholas"
	};
	
	console.log("name" in person1);	// true
	
	delete person1.name;	// true - not output
	console.log("name" in person1); // false
	console.log(person1.name);	// undefined
	 
**Enumeration**
Object.keys() to retrieve the enumerable properties from an object

    var properties = Object.keys(object); 
    
	var i, len;
	
	for (i=0, len=properties.length; i < len; i++){ 
		console.log("Name: " + properties[i]); 
		console.log("Value: " + object[properties[i]]);
	}

## Accessor Properties

 

    var person1 = {
		_name: "Nicholas",

		get name() { 
		 	console.log("Reading name");
			return this._name; 
		},

		set name(value) {
			console.log("Setting name to %s", value);
			this._name = value;
		}
	}; 

	console.log(person1.name);	// "Reading name" then "Nicholas"
	person1.name = "Greg"; 
	console.log(person1.name);	// "Setting name to Greg" then "Greg"
