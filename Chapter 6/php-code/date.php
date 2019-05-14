<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Using Nginx</title>
    <link href="css/bootstrap.min.css" rel="stylesheet">
  </head>
  <body>
      <?php date_default_timezone_set('GMT'); ?>
   <div class="container">
     <div class="jumbotron">
      <h1>Checking dates</h1>
     </div>
     <div class="row">
	<h4>Today is <?php echo "<mark>" . date("l"). "</mark>, ". date("d-M"). " and curent time is " . date("h:i:sa");?></h4></div>
    <div class="row">
	<h4> Tomorrow will be 
	<?php $d=strtotime("tomorrow"); echo date("l", $d) .", ".date("d-M", $d) . ".";?></h4></div>
    <div class="row">
	<h4> Next Sunday is on  
	<?php $d=strtotime("next Sunday");echo date("d-M", $d) .".";?></h4></div>
   </div> 
 </body>
</html>
