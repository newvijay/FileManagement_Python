# FileManagement_Python

Implemented a FileSystem class.
Notes:
Root path is '/'.
Path separator is '/'.
Parent directory is addressable as '..'.
Directory names consist only of English alphabet letters (A-Z and a-z).
All functions support both relative and absolute paths.
All function parameters are the minimum required/recommended parameters.
Did not used built-in path-related functions or third party libraries.


Sample output:
$fs = new FileSystem(); 
$fs->mkdir('usr'); 
$fs->cd('usr'); 
$fs->mkdir('local'); 
$fs->cd('local'); 
echo $fs->pwd(); 
 
>> /usr/local 
 
$fs->cd('..'); 
$fs->mkdir('share'); 
$fs->mkdir('share/info'); 
$fs->cd('share/info'); 
echo $fs->pwd(); 
 
>> /usr/share/info 
 
$fs->mkdir('/usr/local/log'); 
$fs->cd('/usr/local/log'); 
echo $fs->pwd(); 
 
>> /usr/local/log 
 
$fs->mkdir('some/folder') 
 
>> folder "some" does not exist 
 
$fs->cd('/usr/unknown/folder'); 
 
>> folder "unknown" does not exi
