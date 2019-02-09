![](https://i.imgur.com/Vuhtexl.jpg)

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
python3 ddump.py -u hackerone.com --all
```
or
```bash
./ddump.py -u hackerone.com --all
```
or
```python
import dnsdmpstr

target = "hackerone.com"

dnsdump = dnsdmpstr()
print(json.dumps(dnsdump.dump(target), indent=1))
print(dnsdump.hostsearch(target))
print(dnsdump.reversedns(target))
print(dnsdump.dnslookup(target))
print(dnsdump.pagelinks(target))
print(dnsdump.httpheaders(target))
```
