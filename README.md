# PLAD
PLAD is a secure password manager that uses a [RSA](https://www.comparitech.com/blog/information-security/rsa-encryption/) encryption for saving your passwords. It works on a terminal using python 3.9 or higher. It's simple to use and very powerful.
You don't need to remember all of your passwords or making the mistake of using the same password on all your accounts. You can create a completely random password for an e-mail account, a social network or everything else and save it on your device! You can define how long do you want the password to be and the usage of symbols or not.

The user just need to define 2 private keys (P and Q) and the program will give another one, called "Master key" (D). These keys are the base of the security algorithm [RSA](https://www.comparitech.com/blog/information-security/rsa-encryption/) and
just with these 3 keys the user can access to every password saved on PLAD.
 
## Requirements

- Python 3.8 / python 3.9 or higher
- Pyfiglet library

## Installation
Clone the program on your computer:
```bash
git clone https://github.com/AlexDurango/PLAD.git
```

Open the folder:
```bash
cd PLAD/
```

And run PLAD.py:
### - Windows
```python
python PLAD.py
```

### - Linux
```python
python3 PLAD.py
```

Then, the program will ask you for a range of numbers (Minimun-Value, Maximun-Value) to define your keys P and Q.
You have to type a range like "(100, 250)" or something similar. After that, the program will print the possible keys in the range that you gave. We recomend to use a low range but to choose numbers that are far from each other.

For example, you can choose the range (300, 700) and set the P key as 307 and set the Q key as 691.
The program will return a Master key D. 

**You have to make sure that you can remember these keys (P, Q and Master key D) or if you can't, just write them down**


## Main commands

The main commands to start using PLAD are:

(The commands for linux are the same, just replace "python" for "python3")

- Create a PLAD:
```python
python PLAD.py -C <key_name> <N° characters> <S+ or S- >

#For example

python PLAD.py -C john.doe@gmail.com 15 S+
```

- Search the password of a PLAD:
```python
python PLAD.py -S <key_name>

#For example

python PLAD.py -S john.doe@gmail.com
```

- List the key names on the data base:
```python
python PLAD.py -L
```

- Delete a PLAD:
```python
python PLAD.py -D <key_name>

#For example

python PLAD.py -D john.doe@gmail.com
```

- Print the current version:
```python
python PLAD.py -V
```

- Help command:
```python
python PLAD.py -h
```

## Contact me
Please let me know if there is a bug or some update that you would like to see. You can let me know the issue here on GitHub or send a mail to:

alex.durango2303@gmail.com
