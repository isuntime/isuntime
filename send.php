<?php
header("content-type:text/html;charset=utf-8");  
$dsn="'mysql:dbname=iot;host=localhost'";
$db_user='iot';  
$db_pass='sintianadmin'; 
// try{  
// 	$pdo=new PDO($dsn,$db_user,$db_pass);  
// }catch(PDOException $e){  
// 	echo '数据库连接失败'.$e->getMessage();  
// }
// echo "1";
// $number=rand(20,100);
$sql="update dirverlist set right='10' where system_id='1'";
// if($pdo -> exec($sql)){ 
// 	echo "插入成功！"; 
// 	echo $pdo -> lastinsertid(); 
// }else{
// 	echo "error";
// }
// try{
// 	$pdo = new PDO("mysql:host=10.0.0.3;dbname=iot","iot","sintianadmin");
// }catch (PDOException $e) {
// 	echo 'Connection failed: ' . $e->getMessage();
// }
//     echo $sql . "";
//     $pdo->query('set names utf8;');
//     $result = $pdo->query($sql);
//     $rows = $result->fetchAll();
//     foreach ($rows as $row) {
//         $username = $row[1];
//         $pwd = $row[2];
//         echo $username;
//     }
$mysql = new mysqli();
echo "11";
?>