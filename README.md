# RAMMonitoringTool (Python)
## Recieve an email if one of your Servers' RAM usage goes over a set value (%)
## I'm merging fixes, send me a pull request.
Python Script to monitor RAM usage in Remote Computer.

### It depends on psutil (https://pypi.org/project/psutil/)

### For remote use, use cat and SSH as follows:
#### cat hello.py | ssh user@192.168.1.101 python - arg1 arg2 arg3

### Quick Description

1 - Script will capture SMTP Username, and SMTP Password to send email if RAM goes higher than set limit.

2 - Script will check Local System (Wherever is run) every second.

### Code is well documented, please take a look.
