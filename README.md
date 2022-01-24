
# A chat using sockets in Python
My first ever networking project with sockets in python.
Its not that good, so please don't judge :D

### Features
* A small encryption defined in the `encrpyted` and `decrypted` function.
* A special command `/w` to whisper to a specific person who is connected.

    Usage: `/w <name> <message>`
* ANSI colours
#
![username](https://github.com/MonstrousMidget9/terminal-based-chat/blob/main/readme/username.png?raw=true)

![mainchat](https://user-images.githubusercontent.com/70360354/149001276-9866bbc2-f148-4e99-88eb-4cfd6dd0dc58.png)
#
__Note__: Change the localhost in `sock.bind` (to 0.0.0.0 or by manually typing the local ip) when port forwarding or using a virtual server to accept inbound connections from outside the LAN.
