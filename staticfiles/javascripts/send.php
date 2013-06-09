<?php

$name	  = $_POST['name'];
$email	  = $_POST['email'];
$message  = $_POST['message'];

$to       = "daniel@danielpost.nl";
$subject  = "Message from one of your visitors";
$headers  = "From: $email";
$body     = "Name: $name \n\n $message";

mail($to, $subject, $body, $headers);
?>