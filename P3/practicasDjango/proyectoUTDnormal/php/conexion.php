<?php
  $servidor="localhost";
  $usuario="root";
  $password="";
  $bd="bd_proyectoutd";
  $puerto=8080;

   //Conexion Orientada a Objetos
  //$conexion=new mysqli($servidor,$usuario,$password,$bd);

  //Conexion Procedural
  $conexion=mysqli_connect($servidor,$usuario,$password,$bd);
 

?>