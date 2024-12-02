<?php
session_start();

// Verificar si existen variables de sesión
if (isset($_SESSION)) {
  
    session_destroy();

    
    setcookie("mensaje", "cerro_sesion", time() + 5, "/"); 
    header("Location: ../index.php");
    exit();
}
?>
