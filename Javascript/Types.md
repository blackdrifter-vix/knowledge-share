
# Javascript Notes

# Primitive and Reference Types

Javascript is of 2 types:

**Primitive** - stored as simple data types

**Reference** - stored as objects, which are really just references to locations in memory.

 # Primitive Type
**Primitive types :** Boolean, Number, String, Null, Undefined

  
Identifying primitive types using  **console.log(_typeof {variable})_**

  

**_console.log(typeof null)_** returns **object** although null is a data type

 
Primitive Methods: (_Despite the fact that they have methods, primitive values themselves are not objects._)

.toSting()

.toLowerCase()

.charAt()

.toFixed()

  

# Reference Type

Create Objects:

to instantiate an object, first is to use **new** operator with a constructor

_var object = new Object();_

this do not store object in variable like primitive. It holds a pointer to the location in memory where the object exists

  

**Dereferencing Objects**

It’s best to _dereference_ objects that you no longer need so that the garbage collector can free up that memory.

var object1 = new Object();  
// do something  
object1 = null; // dereference

  

**Instantiating built-in Types**

Example:

	var items = new Array();  
	var now = new Date();  
	var error = new Error("Something bad happened.");

	var func = new Function("console.log('Hi');");

	var object = new Object();  
	var re = new RegExp("\\d+");

  

  

**Identifying Reference Types**

The instanceof operator allows to check whether an object belongs to a certain class. It also takes inheritance into account.

> obj instanceof Class

  

Example:

	var items = [];
	var object = {};
	
	function reflect(value) {
		return value;
	}
	
	console.log(items instanceof Array); // true
	console.log(object instanceof Object); // true
	console.log(reflect instanceof Function); // true

  

**Primitive wrapper Types**

The primitive wrapper types are reference types that are automatically created behind the scenes whenever strings, numbers, or Booleans are read.

Example:

	var name = "Nicholas";
	name.last = "Zakas";

	console.log(name.last); // undefined

  

**what the JavaScript engine does**

	var name = "Nicholas";
	var temp = new String(name);
	temp.last = "Zakas";
	temp = null;  // temporary object destroyed
	
	var temp = new String(name);
	console.log(temp.last);  // undefined
	temp = null;