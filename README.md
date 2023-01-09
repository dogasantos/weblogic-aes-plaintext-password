# weblogic-aes-plaintext-password

## step 1
find setWLSEnv.sh script and execute it

## step 2
place the getpw.py on the server (yeap, you need shell on target server, with an user with permission to read weblogic domain files)

## step 3
replace "{AES}STRING" in the getpw.py code, to the proper string you found


## step 4
run this:

java weblogic.WLST getpw.py

You should see something like this:

```
Initializing WebLogic Scripting Tool (WLST) ...

Welcome to WebLogic Server Administration Scripting Shell

Type help() for help on available commands

Plain Text password is: ClearTextPasswordHere
```
