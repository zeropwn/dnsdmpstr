![](http://i.imgur.com/gxIlGAl.gif)

# dnsdmpstr
Unofficial API &amp; Client for https://dnsdumpster.com/

# Installation
```bash
git clone https://github.com/zeropwn/dnsdmpstr
cd dnsdmpstr
chmod +x dnsdmpstr.py
```

# Usage
```bash
python3 dnsdmpstr.py
```
or
```bash
./dnsdmpstr.py
```
or
```python
import dnsdmpstr

dnsdump = dnsdmpstr()
print(dnsdump.dump('hackforums.net')) # prints a dictionary containing the information
```
