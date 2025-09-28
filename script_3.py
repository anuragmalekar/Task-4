# Create common ports and security implications reference
ports_data = {
    'Port_Number': [21, 22, 23, 25, 53, 80, 110, 143, 443, 993, 995, 1433, 3389, 5432, 8080],
    'Protocol': ['TCP', 'TCP', 'TCP', 'TCP', 'UDP/TCP', 'TCP', 'TCP', 'TCP', 'TCP', 'TCP', 'TCP', 'TCP', 'TCP', 'TCP', 'TCP'],
    'Service_Name': ['FTP', 'SSH', 'Telnet', 'SMTP', 'DNS', 'HTTP', 'POP3', 'IMAP', 'HTTPS', 'IMAPS', 'POP3S', 'SQL Server', 'RDP', 'PostgreSQL', 'HTTP Alt'],
    'Common_Use': ['File Transfer', 'Secure Shell Remote Access', 'Terminal Access', 'Email Sending', 'Domain Name Resolution', 
                   'Web Traffic', 'Email Retrieval', 'Email Access', 'Secure Web Traffic', 'Secure Email Access', 
                   'Secure Email Retrieval', 'Database Access', 'Remote Desktop', 'Database Access', 'Alternative Web'],
    'Security_Risk': ['High', 'Medium', 'Very High', 'Medium', 'Low', 'Medium', 'High', 'Medium', 'Low', 'Low', 
                     'Low', 'High', 'High', 'High', 'Medium'],
    'Default_Action': ['Block', 'Allow (with restrictions)', 'Block', 'Block (external)', 'Allow', 'Allow', 'Block', 'Block', 
                      'Allow', 'Allow', 'Allow', 'Block (external)', 'Block (external)', 'Block (external)', 'Allow'],
    'Firewall_Rule_Reason': [
        'Unencrypted file transfers, credential exposure',
        'Secure but limit to trusted IPs, enable fail2ban',
        'Unencrypted, credentials sent in plaintext',
        'Open relay risks, spam potential',
        'Essential for web browsing and domain resolution',
        'Standard web traffic, but monitor for attacks',
        'Unencrypted email retrieval',
        'Email access, prefer encrypted alternatives',
        'Encrypted web traffic, generally safe',
        'Encrypted email access, secure',
        'Encrypted email retrieval, secure',
        'Database should not be externally accessible',
        'Remote access should be restricted/VPN only',
        'Database should not be externally accessible',
        'Alternative web port, monitor for unauthorized services'
    ],
    'Recommended_Config': [
        'Block or use SFTP/FTPS instead',
        'Allow with IP restrictions + key auth',
        'Block completely, use SSH instead',
        'Block external, allow internal only',
        'Allow but monitor for DNS amplification',
        'Allow with WAF protection',
        'Block, use POP3S (995) instead',
        'Allow but prefer IMAPS (993)',
        'Allow with proper certificate validation',
        'Allow for secure email clients',
        'Allow for secure email clients',
        'Block external, allow internal networks only',
        'Block external, use VPN for remote access',
        'Block external, allow internal networks only',
        'Monitor and restrict to authorized applications'
    ],
    'Testing_Command': [
        'telnet host 21',
        'ssh user@host',
        'telnet host 23',
        'telnet host 25',
        'nslookup domain host',
        'curl http://host',
        'telnet host 110',
        'telnet host 143',
        'curl https://host',
        'openssl s_client -connect host:993',
        'openssl s_client -connect host:995',
        'telnet host 1433',
        'mstsc (Windows) or rdesktop (Linux)',
        'psql -h host -p 5432',
        'curl http://host:8080'
    ]
}

df_ports = pd.DataFrame(ports_data)
df_ports.to_csv('common_ports_security_reference.csv', index=False)
print("Created common_ports_security_reference.csv")

# Display summary of high-risk ports
high_risk = df_ports[df_ports['Security_Risk'].isin(['High', 'Very High'])]
print("\nHigh-Risk Ports Summary:")
print(high_risk[['Port_Number', 'Service_Name', 'Security_Risk', 'Default_Action']].to_string(index=False))