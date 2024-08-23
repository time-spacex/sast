<?php
if (isset($_GET['file'])) {
    $file = $_GET['file'];
    
    // File Inclusion vulnerability
    include($file);
}

echo "This is a safe operation";
?>
