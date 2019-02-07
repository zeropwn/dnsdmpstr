![](https://i.imgur.com/Wu3tEEq.jpg)

# dnsdmpstr
Unofficial API &amp; Client for https://dnsdumpster.com/

# Installation
```bash
git clone https://github.com/zeropwn/dnsdmpstr
cd dnsdmpstr
pip3 install -r requirements.txt
chmod +x ddump.py
```

# Usage
```bash
python3 ddump.py hackerone.com
```
or
```bash
./ddump.py hackerone.com
```
or
```python
import dnsdmpstr

dnsdump = dnsdmpstr()
print(dnsdump.dump('hackforums.net')) # prints a dictionary containing the information
```
