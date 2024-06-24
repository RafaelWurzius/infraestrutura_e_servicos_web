<?php
error_reporting(0);

$username = $_POST['username'];
$password = $_POST['password'];

$url = 'http://192.168.15.3:5000/login';

$data = array('username' => $username, 'password' => $password);

$options = array(
    'http' => array(
        'header'  => "Content-type: application/json\r\n",
        'method'  => 'POST',
        'content' => json_encode($data),
    ),
);

$context  = stream_context_create($options);
$result = file_get_contents($url, false, $context);
$response = json_decode($result, true);

if ($response['status'] == 'success') {
    header('Location: http://192.168.15.4:8000/home.php');

} else {
    echo "Login failed. " . $response['message'];
}
?>
