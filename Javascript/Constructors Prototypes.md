
# Javascript Notes

# Constructors and Prototypes

A constructor is simply a function that is used with ***new*** to create an object.

    function Person() {
     // intentionally empty 
    }
   This function is a constructor. Person is a constructor is in the name—the first letter is capitalized.
   After the constructor is defined, you can start creating instances, like the following two Person objects:
   

    var person1 = new Person();
    var person2 = new Person();
    
	var person1 = new Person;
	var person2 = new Person;	
	
Function with Properties:

	function Person(name) {
		this.name = name;
		this.sayName = function() {
			console.log(this.name);
		};
	}
    
	var person1 = new Person("Nicholas");
	var person2 = new Person("Greg");
	console.log(person1.name);	// "Nicholas"
	console.log(person2.name);	// "Greg"
	person1.sayName(); 	// outputs "Nicholas"
	person2.sayName();	// outputs "Greg"
## Prototypes
A *prototype* as a recipe for an object. Almost every function (with the exception of some built-in functions) has a prototype property that is used during the creation of new instances.
For example, the **hasOwnProperty()** method is defined on the generic Object prototype.

**Using Prototypes with Constructors**

    function Person(name) { 
		this.name = name;
	}

	Person.prototype.sayName = function() { 
		console.log(this.name);
	};

	var person1 = new Person("Nicholas");	
	var person2 = new Person("Greg"); 

	console.log(person1.name);	// "Nicholas"
	console.log(person2.name);	// "Greg"

	person1.sayName(); 	// outputs "Nicholas"
	person2.sayName();	// outputs "Greg"
 
 
