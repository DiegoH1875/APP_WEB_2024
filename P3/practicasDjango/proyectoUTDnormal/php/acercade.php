<?php
session_start();
            if (isset($_SESSION['user'])) {
                
            } else {
                header("Location: ../index.php");
                exit();
            }
            ?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>
        Inicio|PHP Proyecto UTD
    </title>
    <link rel="stylesheet" href="../css/estilos.css" type="text/css">
</head>
<body>
    <header>
        <div id="logotipo">
            <img src="../img/logophp.png" alt="Imagen Django" title="Django">
            <h1>PHP Proyecto Web</h1>
        </div>
    </header>
    <nav>
        <ul>
                <li><a href="../index.php" >Inicio</a></li>
                <li><a href="mision.php">Misión</a></li>
                <li><a href="vision.php">Visión</a></li>
                <li><a href="acercade.php">Acerca de</a></li>
                <li><a href="mostrar_articulos.php">Artículos</a></li>
                <li><a href="mostrar_categorias.php">Categorías</a></li>
                <li><a href="cerrar_sesion.php">Cerrar sesión</a></li>
        </ul>
    </nav>
    <section id="content">
       <div class="box">
            <h1>Acerca de </h1>
            <hr>
            <p>Somos una universidad formada en Durango</p>
       </div>
    </section>
    <footer>
        <p>Desarrollador Web</p>
    </footer>
</body>
</html>