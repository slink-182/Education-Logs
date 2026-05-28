# 002 VTP

| Purpose                                   | Command                   |
| :---------------------------------------- | ------------------------: |
| Set VTP domain name                       | `vtp domain <name>`       |
| Set switch as VTP server                  | `vtp mode server`         |
| Set switch as VTP client                  | `vtp mode client`         |
| Set switch as VTP transparent             | `vtp mode transparent`    |
| Disable VTP (some platforms)              | `vtp mode off`            |
| Set VTP password                          | `vtp password <password>` |
| Set VTP version                           | `vtp version 1`           |
|                                           | `vtp version 2`           |
|                                           | `vtp version 3`           |
| Enable VTP pruning                        | `vtp pruning`             |
| Disable VTP pruning                       | `no vtp pruning`          |
| Set VTPv3 primary server                  | `vtp primary vlan`        |
| Specify VLAN database file                | `vtp file <filename>`     |
| Enable VTP on interface                   | `vtp interface`           |
| Disable VTP on interface                  | `no vtp`                  |
| Show VTP status                           | `show vtp status`         |
| Show VTP statistics/counters              | `show vtp counters`       |
| Show VTP neighbors/devices                | `show vtp devices`        |
| Show configured VTP password              | `show vtp password`       |
| Show VTP interface details                | `show vtp interface`      |
| Show VTP conflicts                        | `show vtp conflicts`      |
| Enter VLAN database mode (older IOS)      | `vlan database`           |
| Configure VTP server in VLAN DB mode      | `vtp server`              |
| Configure VTP client in VLAN DB mode      | `vtp client`              |
| Configure VTP transparent in VLAN DB mode | `vtp transparent`         |
| Configure VTP domain in VLAN DB mode      | `vtp domain <name>`       |

Link sourcing material: https://www.cisco.com/c/en/us/support/docs/lan-switching/vtp/98154-conf-vlan.html