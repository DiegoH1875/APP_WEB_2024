//Este es un comentario de JavaScript de una línea

/* Este es un comentario de 
varias
lineas de código
*/

// V A R I A B L E S
//let se puede cambiar y var es como una constante
var nombre = "Diego Sierra Alcala";
var nombre2 = 'Francisco Perez Figueroa';
let nombre3 = "Sexon Rodrigo";
let edad = 20;
let estatura = 1.80
let logico = true;

//Mostrar contenido de variables
console.log("Hola, soy la consola y tu nombre es: " + nombre)  //A traves de consola
document.write("Hola, soy la consola y tu nombre es: " + nombre)
document.write("<hr><h2> Hola, soy la consola y tu nombre es: " +nombre+"</h2></hr>")
alert("Soy una alerta" +nombre);


//Mostrar contenido getElementById
let datos = document.getElementById("informacion");
datos.innerHTML= "Hola soy in contenido de innerHTML <br>"
datos.innerHTML += "<hr><h2>Hola soy otro contenido de innerHTML</h2><hr>"
datos.innerHTML += "<hr><h2>Mi edad es: " +edad+ "</h2><hr>";
datos.innerHTML += `
            <hr>
            <h2>Mi edad es: ${edad}</h2>
            <h2>Mi nombre es: ${nombre}</h2>
            </hr>
`; 

//Condiciones
if (edad >= 18)
{
    datos.innerHTML += <hr><h2>Soy mayor de edad</h2></hr>;
}
else
{
    datos.innerHTML += <hr><h2>Soy menor de edad</h2></hr>;
}


//ciclos
for(let i=1;i<=5;i++);
{
    datos.innerHTML += <hr><h2>For: soy el numero ${i}</h2></hr>;
}

let i = 1;
while(i <=5);{
    datos.innerHTML += <hr><h2>While: soy el numero ${i}</h2></hr>;
    i++
}

i=1;
do{
    datos.innerHTML += <hr><h2>Do While: soy el numero ${i}</h2></hr>;
    i++;
}while(i <= 5);

// Arreglos
let animales = [];
animales[0]="Perro";
animales[1]="Gallina";
animales[2]="Perico";

let animales2 = ["Tigre", "Elefante", "Tigre"];

for(let i=0; i < animales.length; i++)
{
    datos.innerHTML += `<hr><h2> El animal es : ${animales[i]}</h2></hr>`;
}