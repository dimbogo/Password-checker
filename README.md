# Password-checker
This script allows you to check if your password has been hacked using the most safe way
<br>
<h1>How it works</h1><br>
-Create a txt file with space-separated list of passwords you want to check (might be on different lines as well)<br>
-Place the script file in the same folder with the txt file<br>
-Run the file through a terminal giving the name of txt file as an argument (e.g. ...\ <b>python checkmypass.py passwords.txt</b>)<br>
<br>
<h2>Why it's safe?</h2><br>
1) Your password is encrypted by SHA1 algorithm<br>
2) The sciprt never imports your password fully to the third-party API, just a tiny bit of it<br>
3) The password is not been stored anywhere except the RAM of your computer throughout the script execution and the original txt file (which you should obviously delete right after you've finished)
