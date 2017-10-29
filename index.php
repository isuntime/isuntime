<?php
//phpinfo();
header("content-type:text/html;charset=utf-8"); 
try{
	$pdo = new PDO('mysql:host=10.0.0.3;dbname=iot;port=3306','iot','sintianadmin');
}catch (PDOException $e) {
        echo 'Connection failed: ' . $e->getMessage();
}
$pdo->exec('set names utf8');
$stmt = $pdo->prepare("select * from dirverlist");
$stmt->bindValue(':id',1,PDO::PARAM_INT);
$stmt->execute();
$rows = $stmt->fetchAll(PDO::FETCH_ASSOC);
$rows = $pdo->query("dirverlist")->fetchAll(PDO::FETCH_ASSOC);
echo "1";
?>
