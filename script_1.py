# Create firewall rules documentation
firewall_rules = {
    'Rule_ID': ['WIN_R001', 'WIN_R002', 'WIN_R003', 'LIN_R001', 'LIN_R002', 'LIN_R003'],
    'Platform': ['Windows', 'Windows', 'Windows', 'Linux', 'Linux', 'Linux'],
    'Rule_Name': ['Block Telnet Port 23', 'Allow SSH Port 22 Inbound', 'Allow SSH Port 22 Outbound', 
                 'Deny Telnet', 'Allow SSH', 'Default Deny Incoming'],
    'Direction': ['Inbound', 'Inbound', 'Outbound', 'Inbound', 'Inbound', 'Inbound'],
    'Action': ['Block', 'Allow', 'Allow', 'Deny', 'Allow', 'Deny'],
    'Protocol': ['TCP', 'TCP', 'TCP', 'TCP', 'TCP', 'All'],
    'Port': [23, 22, 22, 23, 22, 'All'],
    'Source': ['Any', 'Any', 'Local', 'Any', 'Any', 'Any'],
    'Destination': ['Local', 'Local', 'Any', 'Local', 'Local', 'Local'],
    'Profile': ['All', 'All', 'All', 'All', 'All', 'All'],
    'Command_Used': [
        'netsh advfirewall firewall add rule name="Block Telnet Port 23" dir=in action=block protocol=TCP localport=23',
        'netsh advfirewall firewall add rule name="Allow SSH Port 22" dir=in action=allow protocol=TCP localport=22',
        'netsh advfirewall firewall add rule name="Allow SSH Port 22 Outbound" dir=out action=allow protocol=TCP localport=22',
        'sudo ufw deny 23/tcp',
        'sudo ufw allow ssh',
        'sudo ufw default deny incoming'
    ],
    'Status': ['Created & Tested', 'Created & Tested', 'Created & Tested', 'Created & Tested', 'Created & Tested', 'Active'],
    'Removal_Command': [
        'netsh advfirewall firewall delete rule name="Block Telnet Port 23"',
        'netsh advfirewall firewall delete rule name="Allow SSH Port 22"',
        'netsh advfirewall firewall delete rule name="Allow SSH Port 22 Outbound"',
        'sudo ufw delete deny 23/tcp',
        'sudo ufw delete allow ssh',
        'sudo ufw default allow incoming'
    ],
    'Purpose': ['Testing port blocking functionality', 'Enable SSH access for remote management', 
               'Allow outbound SSH connections', 'Testing UFW port blocking', 
               'Maintain remote access via SSH', 'Default security posture']
}

df_firewall_rules = pd.DataFrame(firewall_rules)
df_firewall_rules.to_csv('firewall_rules_documentation.csv', index=False)
print("Created firewall_rules_documentation.csv")
print(df_firewall_rules[['Rule_ID', 'Platform', 'Rule_Name', 'Action', 'Protocol', 'Port', 'Status']].to_string(index=False))