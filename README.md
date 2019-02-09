![](https://i.imgur.com/Vuhtexl.jpg)

# dnsdmpstr
Unofficial API & Client for DNS Dumpster and HackerTarget.com IP tools.
* https://dnsdumpster.com/
* https://hackertarget.com/ip-tools/

## Installation
```bash
git clone https://github.com/zeropwn/dnsdmpstr
cd dnsdmpstr
pip3 install -r requirements.txt
chmod +x ddump.py
```

## Usage

### As a command-line utility
```bash
target="hackerone.com"
python3 ddump.py -u $target --all
```

#### Extended usage
```
usage: ddump.py [-h] [-u U] [-a] [-r] [-d] [-dd] [--links] [--headers] [--all]

optional arguments:
  -h, --help  show this help message and exit
  -u U        target domain
  -a          host search (DNS A Record lookup)
  -r          reverse dns lookup (accepts IP, IP range or domain name)
  -d          dns lookup
  -dd         classical dns dump format
  --links     grab page links from url
  --headers   grab http headers from url
  --all       grab all information available
```

### As a library
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
