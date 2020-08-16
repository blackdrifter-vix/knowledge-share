
# Javascript Notes

# Functions

**Declarations vs. Expressions**
**Declaration**

    function add(num1, num2) {
    	return num1 + num2; 
    }
  **Expression**
  

    var add = function(num1, num2) { 
	    return num1 + num2;
	};

JavaScript engine hoists the function declaration to the top so we can declare functions anywhere in javascript file and can be declared anywhere within the same file without respect to any position.

Function hoisting happens only for function declarations because the function name is known ahead of time. Function expressions, on the other hand, cannot be hoisted because the functions can be referenced only through a variable.

# Functions as Values
You can assign them to variables, add them to objects, pass them to other functions as arguments, and return them from functions.

    function sayHi() { 
	    console.log("Hi!");
	}
	sayHi(); // outputs "Hi!" 
	
	var sayHi2 = sayHi;
	sayHi2(); // outputs "Hi!"

For instance, suppose you want to create a function that accepts any number of parameters and returns their sum. You can’t use named parameters because you don’t know how many you will need, so in this case, using arguments is the best option.

    function sum() { 

		var result = 0, 
			i = 0,
			len = arguments.length;

		while (i < len) {  
			result += arguments[i]; i++;
		}

		return result;
	} 

	console.log(sum(1, 2));		// 3
	console.log(sum(3, 4, 5, 6));		// 18
	console.log(sum(50)); 		// 50
	console.log(sum());			// 0

	
# Overloading

    function sayMessage(message) { 
	    console.log(message);
	}

	function sayMessage() { 
		console.log("Default message");
	}  
	
	sayMessage("Hello!"); 	// outputs "Default message"

In another language, the output of sayMessage("Hello!") would likely be "Hello!"
In Javascript, the one that appears last in your code wins. Earlier function declarations are completely removed.

# The this Object

    var person = {  
		name: "Nicholas",
		sayName: function() {
			console.log(this.name);
		}
	};  
	
	person.sayName(); // outputs "Nicholas"

# Changing this
## call() Method
call(), which executes the function with a particular this value and with specific parameters.

    function sayNameForAll(label) { 
	    console.log(label + ":" + this.name);
    }
    
    var person1 = { 
	    name: "Nicholas"
    };
    
    var person2 = { 
	    name: "Greg"
    };  
    
    var name = "Michael";
    
    sayNameForAll.call(this, "global"); // outputs "global:Michael"
    sayNameForAll.call(person1, "person1"); // outputs "person1:Nicholas"
    sayNameForAll.call(person2, "person2"); // outputs "person2:Greg"
    
## apply() Method
apply() method works exactly the same as call() except that it accepts only two parameters: the value for this and an array or array-like object of parameters to pass to the function

    function sayNameForAll(label) { 
	    console.log(label + ":" + this.name);
	}

	var person1 = { 
		name: "Nicholas"
	};

	var person2 = { 
		name: "Greg"
	};  
	var name = "Michael";

	sayNameForAll.apply(this, ["global"]);  // outputs "global:Michael"
	sayNameForAll.apply(person1, ["person1"]); // outputs "person1:Nicholas" 
	sayNameForAll.apply(person2, ["person2"]); // outputs "person2:Greg"

## bind() Method
The first argument to bind() is the this value for the new function. All other arguments represent named parameters that should be permanently set in the new function.

    let user= { 
	    firstName:  "John"
	};
	  
    function func(){  
	    alert(this.firstName);  
	}
	
	let funcUser = func.bind(user);
	funcUser(); // John

**Partial Functions**

    function mul(a, b) {
	  return a * b;
	}

	let double = mul.bind(null, 2);

	alert( double(3) ); // = mul(2, 3) = 6
	alert( double(4) ); // = mul(2, 4) = 8
	alert( double(5) ); // = mul(2, 5) = 10
The call to `mul.bind(null, 2)` creates a new function `double` that passes calls to `mul`, fixing `null` as the context and `2` as the first argument.
Please note that here we actually don’t use `this` here. But `bind` requires it, so we must put in something like `null`.