# 001 SHOW COMMANDS

Knowing how to check current configurations can help you correct errors in your setup. The following table shows the commands used to check problems:

| Problem | Command |
| :- | -: |
| Port down	| show ip interface brief |
| VLAN missing | show vlan brief |
| Trunk missing	show | interfaces trunk |
| Wrong port mode | show interfaces switchport |
| VTP not syncing | show vtp status |
| Wrong uplink | show cdp neighbors |
| Traffic not learned | show mac address-table |
| STP blocking | show spanning-tree |

### Note: I'll likely be referencing this table quite a lot during my Network Design course, and into the future with network setup and trouble shooting.