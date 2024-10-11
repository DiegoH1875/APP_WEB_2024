function operacion(event) {
    // Evitar que el formulario se envíe
    event.preventDefault();
    
    // Obtener los valores de los campos de entrada
    let n1 = parseFloat(document.getElementById('N1').value);
    let n2 = parseFloat(document.getElementById('N2').value);
    let operacion = document.getElementById('Operaciones').value;

    let resultado;
    let simbolo_operacion;

    if (is_number(n1) && is_number(n2))
    {
        // Realizar la operación según la selección
        if (operacion === "suma") 
        {
            resultado = n1 + n2;
            simbolo_operacion = "+"
        } 
        else if (operacion === "resta") 
        {
            resultado = n1 - n2;
            simbolo_operacion = "-"
        } 
        else if (operacion === "multiplicacion") 
        {
            resultado = n1 * n2;
            simbolo_operacion = "*"
        } 
        else if (operacion === "division") 
        {
            // Verificar si n2 no es cero para evitar la división por cero
            if (n2 !== 0) 
            {
                resultado = n1 / n2;
                simbolo_operacion = "/"
            } 
            else 
            {
                resultado = "Error: División por cero";
            }
        }
        document.getElementById('resultado').innerText = n1 + simbolo_operacion + n2 + "=" + resultado;
    }
    else
    {
        alert("Disculpe, introduzca solamente numeros");
    }

}

function is_number(n)
{
    return !isNaN(parseFloat(n) && isFinite(n))
}