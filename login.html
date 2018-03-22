<!DOCTYPE html>
<?php
$NodeData = array(
);

function displayIP($NodeData,$nodeid)
{

    $count = count($NodeData);
    for ($i = 0; $i < $count; $i++) {
        if($NodeData[$i]['id'] == $_SESSION['nodeid'])
        {
            $DISPLAYip = $NodeData[$i]['name'];
            $DISPLAYip .= '-';
            $DISPLAYip .= $NodeData[$i]['ipx'];
            break;
        }

    }
    return ($DISPLAYip);
}



session_start(); 
if(isset($_GET['argument1'])) 
{
    $_SESSION['nodeid'] =  $_GET['argument1']; // store session data
    $DISPLAYip = displayIP($NodeData,$_SESSION['nodeid']);
   $_SESSION['attackpath'] = './scratchpad/shellscripttrial/';
}

$DISPLAYip = displayIP($NodeData,$_SESSION['nodeid']);




function ssh2command($command,$NodeData,$nodeid,$passargument,$cmdoptions)
{

    $count = count($NodeData);
    for ($i = 0; $i < $count; $i++) {
        if($NodeData[$i]['id'] == $nodeid)
        {
            $nodeIP = $NodeData[$i]['ip'];
            $nodeuser = $NodeData[$i]['user'];
            $nodepassword = $NodeData[$i]['password'];
            break;
        }

    }

$connection = ssh2_connect($nodeIP, 22);

$taret  = ssh2_auth_password($connection,$nodeuser, $nodepassword); 
/*
if($passargument == 1)
{
    $stream = ssh2_exec($connection, $command.' '.$nodepassword.' '.$cmdoptions); 
}
else
{
    $stream = ssh2_exec($connection, $command); 
}  

stream_set_blocking($stream, true);
$stream_out = ssh2_fetch_stream($stream, SSH2_STREAM_STDIO);
$resultcmd = stream_get_contents($stream_out); */
//sanood
		if($passargument == 1)
		{
		    
		    $command_capture = $command.' '.$nodepassword.' '.$cmdoptions;
		    $stream = ssh2_shell($connection);

		    fwrite($stream, $command_capture. PHP_EOL);
		    sleep(10);
		    fwrite($stream,"\x03". PHP_EOL);
		    sleep(1);
		    $resultcmd="";
		        while (true){
			$outdata = stream_get_contents($stream);
			 $resultcmd .= $outdata;
			if (strpos($outdata,"XOXO") !== false) {
			    $resultcmd .= "okay: command finished\n";
			    break;
			}
		    }		    

		    fclose($stream);

		    //$stream = ssh2_exec($connection, $command.' '.$nodepassword.' '.$cmdoptions); 

		}
		else
		{

		    $stream = ssh2_exec($connection, $command); 

			stream_set_blocking($stream, true);
			$stream_out = ssh2_fetch_stream($stream, SSH2_STREAM_STDIO);
			$resultcmd = stream_get_contents($stream_out);

		}  
//sanood

//ssh2_scp_recv($connection, '/home/edsys/anjali.txt', '/home/sanu/scratchpad/testphp/anjali.txt');
return($resultcmd);
}




if(isset($_POST['submit'])) 
{
$inp = $_POST['any_name'];   // Here $var is the input taken from user.

$var = ssh2command($inp,$NodeData,$_SESSION['nodeid'],0,0);
}

?>
<html lang="en">
  <head>
    <style>
    * {text-rendering: optimizeLegibility; font-size:100%;}
    svg g g {font-size:20px;}
    table.google-visualization-orgchart-table {
      border-collapse: separate;
    }
    
/* Style The Dropdown Button */
.dropbtn {
    background-color: #4CAF50;
    color: white;
    padding: 16px;
    font-size: 16px;
    border: none;
    cursor: pointer;
}

/* The container <div> - needed to position the dropdown content */
.dropdown {
    position: relative;
    display: inline-block;
}

/* Dropdown Content (Hidden by Default) */
.dropdown-content {
    display: none;
    position: absolute;
    background-color: #f9f9f9;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
}

/* Links inside the dropdown */
.dropdown-content a {
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
}

/* Change color of dropdown links on hover */
.dropdown-content a:hover {background-color: #f1f1f1}

/* Show the dropdown menu on hover */
.dropdown:hover .dropdown-content {
    display: block;
}

/* Change the background color of the dropdown button when the dropdown content is shown */
.dropdown:hover .dropbtn {
    background-color: #3e8e41;
}
</style>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <!-- Meta, title, CSS, favicons, etc. -->
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">    

    <title>ENM&S </title>

    <!-- Bootstrap -->
    <link href="./vendors/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Font Awesome -->
    <link href="./vendors/font-awesome/css/font-awesome.min.css" rel="stylesheet">
    <!-- NProgress -->
    <link href="./vendors/nprogress/nprogress.css" rel="stylesheet">

    <!-- Custom Theme Style -->
    <link href="./build/css/custom.min.css" rel="stylesheet">
  <body class="nav-md">
    <div class="container body">
      <div class="main_container">
        <div class="col-md-3 left_col">
          <div class="left_col scroll-view">
            <div class="navbar nav_title" style="border: 0;">
              <a href="index.html" class="site_title"><i class="fa fa-bar-chart-o"></i> <span>ENM&S</span></a>
            </div>

            <div class="clearfix"></div>

            <!-- menu profile quick info -->
            <div class="profile clearfix">
              <div class="profile_pic">
                <img src="images/img.jpg" alt="..." class="img-circle profile_img">
              </div>
              <div class="profile_info">
                <span>Welcome,</span>
                <h2>Admin</h2>	<!-- The Logged In User Name will come here... -->
              </div>
              <div class="clearfix"></div>
            </div>
            <!-- /menu profile quick info -->

            <br />

            <!-- sidebar menu -->
            <div id="sidebar-menu" class="main_menu_side hidden-print main_menu">
              <div class="menu_section">
                <h3>General</h3>
                <ul class="nav side-menu">
                  <li><a><i class="fa fa-home"></i> Home <span class="fa fa-chevron-down"></span></a>
                    <ul class="nav child_menu">
                      <li><a href="page.php">Dashboard</a></li>                                          
                      <li><a href="network.php">Network Map</a></li>                      
                    </ul>
                  </li>
                  <li><a><i class="fa fa-edit"></i> Statistics <span class="fa fa-chevron-down"></span></a>
                    <ul class="nav child_menu">
                      <li><a href="packet.php">Packet Statistics</a></li>
                      <li><a href="flow.php">Flow Statistics</a></li>
                    </ul>
                  </li>
                  <li><a><i class="fa fa-desktop"></i> Anomalies <span class="fa fa-chevron-down"></span></a>
                    <ul class="nav child_menu">
                      <li><a href="overall_status.php">Overall Status</a></li>
                    </ul>
                  </li>                 
                </ul>
              </div>             

            </div>
            <!-- /sidebar menu -->

            <!-- /menu footer buttons -->
            <div class="sidebar-footer hidden-small">
              <a data-toggle="tooltip" data-placement="top" title="Settings">
                <span class="glyphicon glyphicon-cog" aria-hidden="true"></span>
              </a>
              <a data-toggle="tooltip" data-placement="top" title="FullScreen">
                <span class="glyphicon glyphicon-fullscreen" aria-hidden="true"></span>
              </a>
              <a data-toggle="tooltip" data-placement="top" title="Lock">
                <span class="glyphicon glyphicon-eye-close" aria-hidden="true"></span>
              </a>
              <a data-toggle="tooltip" data-placement="top" title="Logout" href="index.html">
                <span class="glyphicon glyphicon-off" aria-hidden="true"></span>
              </a>
            </div>
            <!-- /menu footer buttons -->
          </div>
        </div>

        <!-- top navigation -->
        <div class="top_nav">
          <div class="nav_menu">
            <nav>
              <div class="nav toggle">
                <a id="menu_toggle"><i class="fa fa-bars"></i></a>
              </div>

              <ul class="nav navbar-nav navbar-right">
                <li class="">
                  <a href="javascript:;" class="user-profile	 dropdown-toggle" data-toggle="dropdown" aria-expanded="false">
                    <img src="images/img.jpg" alt="">Admin
                    <span class=" fa fa-angle-down"></span>
                  </a>
                  <ul class="dropdown-menu dropdown-usermenu pull-right">
                    <li><a href="profile.html"> Profile</a></li>
                    <!--<li>
                      <a href="javascript:;">
                        <span>Settings</span>
                      </a>
                    </li>-->
                    <li><a href="help.html">Help</a></li>
                    <li><a href="index.html"><i class="fa fa-sign-out pull-right"></i> Log Out</a></li>
                  </ul>
                </li>  
                  </ul>
                </li>
              </ul>
            </nav>
          </div>
        </div>
        <!-- /top navigation -->

        <!-- page content -->
        <div class="right_col" role="main">
          <div class="">
            <div class="page-title">
              <div class="title_left">
                <h3><?php echo $DISPLAYip;?> </h3>
				<h2>Web GUI</h2>
              </div>
            </div>

            <div class="clearfix"></div>

            <div class="row">
              <div class="col-md-12 col-sm-12 col-xs-12">
                <div class="x_panel">
                  <div class="x_title">
					<h2>Logs</h2>				  
                    <ul class="nav navbar-right panel_toolbox">
                      <li><a class="collapse-link"><i class="fa fa-chevron-up"></i></a>
                      </li>
                      <li><a class="close-link"><i class="fa fa-close"></i></a>
                      </li>
                    </ul>
                    <div class="clearfix"></div>
                  </div>                  
                  <div class="x_content">
                  
                       <?php

                            if(isset($_POST['logfrom']))
                            {
                            //echo "You have selected :".$_POST['logfrom']; 
                            $logfrom = $_POST['logfrom'] ;
                            $_SESSION['logfrom'] = $_POST['logfrom'] ;
                            }
                            
							?>
             <!--    -->
                       <form id="radiolog" action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST" >

                         </form> 
    <!--    -->
                         <h1>  </h1>

						<?php
                            if(isset($_POST['formCountries']))
                            {
							$option = $_POST['formCountries'] ;
							 $_SESSION['logdirectory'] = $_POST['formCountries'] ;
						    	if($option  == "SNORT")
						    	{
									$_SESSION['logpath'] = "/var/log/snort/";
									#echo $Directory ;
								}
								elseif($option  == "Apache"){
									$_SESSION['logpath'] = "/var/log/apache2/";
										#echo $Directory ;
								}
								elseif($option  == "Other"){
									$_SESSION['logpath'] = "/var/log/other/";
										#echo $Directory ;
								}
								else{
									$_SESSION['logpath'] = " ";
										#echo $Directory ;
								}
						    }
						?>
						
						 <h1>  </h1>
						 <div>
						 
						 <form id = "logs" action="<?php echo htmlentities($_SERVER['PHP_SELF']); ?>" method="post">
						 
						  <input type="radio" onchange='this.form.submit();' name="logfrom" value="local" <?php if ($_SESSION['logfrom']=="local") echo "checked";?> > Local Copy<br>
                          <input type="radio" onchange='this.form.submit();' name="logfrom" value="remote" <?php if ($_SESSION['logfrom']=="remote") echo "checked";?> > From Server<br>
                           <h1>  </h1>
	                        <select name="formCountries" onchange ="SubmitForm('logs');"  >
	                        <option <?php if($_SESSION['logdirectory'] == 'Select'){ php?>selected<?php } php?> value="Select">--Select-- </option>
		                        <option <?php if($_SESSION['logdirectory'] == 'SNORT'){ php?>selected<?php } php?> value="SNORT">SNORT Logs </option>
		                        <option <?php if($_SESSION['logdirectory'] == 'Apache'){ php?>selected<?php } php?> value="Apache">Apache Logs</option>
		                        <option <?php if($_SESSION['logdirectory'] == 'Other'){ php?>selected<?php } php?> value="Other">Other Logs</option>
	                        </select><br>
	                        <noscript><input type="submit" name="formSubmit" type="hidden" value="Submit" ></noscript>
                        </form>
                        </div>
						 <h1>  </h1>	
<?php						 
function generatelistdropdown($command,$NodeData,$nodeid)
{

$lines = ssh2command("ls ".$_SESSION['logpath'],$NodeData,$_SESSION['nodeid'],0,0);
    $line = strtok($lines, PHP_EOL);

    /*do something with the first line here...*/

    while ($line !== FALSE) {
        // get the next line
        $line = strtok(PHP_EOL);
        $resultcmd = $resultcmd.$line;
        /*do something with the rest of the lines here...*/

    }
    //the bit that frees up memory
    strtok('', '');
return($resultcmd);
}
if(isset($_POST['Logs']))
{
$logname = $_POST['Logs'] ;
$logcontents = ssh2command("cat ".$_SESSION['logpath'].$logname,$NodeData,$_SESSION['nodeid'],0,0);
}


?>
			 <form id="viewlogs" action="<?php echo htmlentities($_SERVER['PHP_SELF']); ?>" method="POST">
						 
                          
                          
                          
                        Directory: <input type="text" name="directory" value =<?php echo $_SESSION['logpath'] ; ?>  >
                        
						 <h1>  </h1>	
						 <input type="submit" name="ListLOgs" value="List Logs" />
						 <h1>  </h1>
                       <select name="Logs" onchange ="SubmitForm('viewlogs');">
                        <option value="Select">--Select-- </option>
                       <?php 
                        $lines = ssh2command("ls ".$_SESSION['logpath'],$NodeData,$_SESSION['nodeid'],0,0);
                        $line = strtok($lines, PHP_EOL);

                        /*do something with the first line here...*/
                        //echo '<option value="'.$line.'">'.$line.'</option>';
                        while ($line !== FALSE) {
                            // get the next line
                            
                            echo '<option value="'.$line.'">'.$line.'</option>';
                            $line = strtok(PHP_EOL);
                            /*do something with the rest of the lines here...*/

                        }
                        //the bit that frees up memory
                        strtok('', '');

                        ?>
                        </select>
                        <h5> <?php echo "File:".$logname;?>  </h5> <textarea name=">" style="width:600px; height:300px;"  ><?php echo $logcontents;?>
                        </textarea>
                        </form>
                    
                 
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="clearfix"></div>
<?php						 
if(isset($_POST['AttacksRun']))
{
$attackname = $_POST['Attacks'] ;
$logattack = ssh2command($_SESSION['attackpath'].$attackname,$NodeData,$_SESSION['nodeid'],1,$_POST['IPlist'].' '.$_POST['attackoptions']);
}


?>
            <div class="row">
              <div class="col-md-12 col-sm-12 col-xs-12">
                <div class="x_panel">
                  <div class="x_title">
					<h2>Attacks</h2>				  
                    <ul class="nav navbar-right panel_toolbox">
                      <li><a class="collapse-link"><i class="fa fa-chevron-up"></i></a>
                      </li>
                      <li><a class="close-link"><i class="fa fa-close"></i></a>
                      </li>
                    </ul>
                    <div class="clearfix"></div>
                  </div>                  
                  <div class="x_content">
                    
						 <h1>  </h1>	
					 <form id="viewattacks" action="<?php echo htmlentities($_SERVER['PHP_SELF']); ?>" method="POST">
						Directory: <input type="text" name="directory" value =<?php echo $_SESSION['attackpath'] ; ?>  >
                        
						 <h1>  </h1>	

                       Attack: <select name="Attacks" >
                        <option value="Select">--Select-- </option>
                       <?php 
                        $lines = ssh2command("ls ".$_SESSION['attackpath'],$NodeData,$_SESSION['nodeid'],0,0);
                        $line = strtok($lines, PHP_EOL);

                        /*do something with the first line here...*/
                        //echo '<option value="'.$line.'">'.$line.'</option>';
                        while ($line !== FALSE) {
                            // get the next line
                            
                            echo '<option value="'.$line.'">'.$line.'</option>';
                            $line = strtok(PHP_EOL);
                            /*do something with the rest of the lines here...*/

                        }
                        //the bit that frees up memory
                        strtok('', '');

                        ?>
                        </select>
                        
                        Target: <select name="IPlist" >
                        <option value="Select">--Select-- </option>
                       <?php 
                           $countip = count($NodeData);
                           for ($i = 0; $i < $countip; $i++) {

                 echo '<option value="'.$NodeData[$i]['ipx'].'">'.$NodeData[$i]['name'].'</option>';
                            }
                                   


                        ?>
                        </select>
                        Options: <input type="text" name="attackoptions"  >
                       <input type="submit" name="AttacksRun" value="Run" />
						 <h1>  </h1>
                        <h5> <?php echo "Attack:".$attackname;?>  </h5> <textarea name="attack>" style="width:600px; height:300px;"  ><?php echo $logattack;?>
                        </textarea>
                        </form>
                      
                 
                  </div>
                </div>
              </div>

            
        <!--              -->
          <div class="clearfix"></div>

            <div class="row">
              <div class="col-md-12 col-sm-12 col-xs-12">
                <div class="x_panel">
                  <div class="x_title">
					<h2>Terminal</h2>				  
                    <ul class="nav navbar-right panel_toolbox">
                      <li><a class="collapse-link"><i class="fa fa-chevron-up"></i></a>
                      </li>
                      <li><a class="close-link"><i class="fa fa-close"></i></a>
                      </li>
                    </ul>
                    <div class="clearfix"></div>
                  </div>                  
                  <div class="x_content">
                    <br>  
                        <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST">

                        Command: <input type="text" name="any_name">
                        <input type="submit" name="submit">

                        Output <textarea name=">" style="width:600px; height:200px;"  ><?php echo $var;?>
                        </textarea>

                        </form>
 					                    
                  </div>
                </div>
              </div>
            </div>
          </div>
        <!-- /page content -->

        <!-- footer content -->
        <footer>
          <div class="pull-right">
            <a href="http://www.dese.iisc.ac.in">DESE</a> | <a href="http://www.iisc.ac.in">IISc</a> | ©2018 All Rights Reserved.
          </div>
          <div class="clearfix"></div>
        </footer>
        <!-- /footer content -->
      </div>
    </div>

    <!-- jQuery -->
    <script src="./vendors/jquery/dist/jquery.min.js"></script>
    <!-- Bootstrap -->
    <script src="./vendors/bootstrap/dist/js/bootstrap.min.js"></script>
    <!-- FastClick -->
    <script src="./vendors/fastclick/lib/fastclick.js"></script>
    <!-- NProgress -->
    <script src="./vendors/nprogress/nprogress.js"></script>      
    <!-- Custom Theme Scripts -->
    <script src="./build/js/custom.min.js"></script>
   
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script>
    function SubmitForm(formId) {
    var oForm = document.getElementById(formId);
    if (oForm) {
        oForm.submit(); 
    }
    else {
        alert("DEBUG - could not find element " + formId);
    }
}
</script>
</body>
</html>
