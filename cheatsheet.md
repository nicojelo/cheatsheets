

## Reconaissance

##### nmap scanning

```bash
nmap -open -p- -T4 {ip}
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

## Foothold

##### connecting ssh
```bash
ssh {user}@{ip} -p {port} 
```

##### putting files in the target system
```bash
scp {path to linenum} {user}@{host}:{path} #Example: scp /opt/LinEnum.sh pingu@10.10.10.10:/tmp
```

## PRIVELEGE ESCALATION

##### sudo-able commands

```bash
sudo -l
```
######running bash in vim
```
:shell 
```

## MISC

##### use gdb in checking binary files
##### pwn commandd to check excessive input
##### pwn command to check how many excessive input is actually needed to overwrite certain address

##### in cracking hashes
```bash
hashcat -m {hash algo mode} {hash file path} {wordlist path}
```
https://hashcat.net/wiki/doku.php?id=example_hashes

## REMINDERS

##### Root Reverse Shell Cheat sheet
http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet
