# Create Windows vs Linux firewall comparison
comparison_data = {
    'Feature': ['Firewall Name', 'Access Method', 'Enable/Disable', 'List Rules', 'Allow Port', 'Block Port', 
               'Allow Service', 'Block Service', 'Default Policy', 'Delete Rule', 'Reset to Defaults',
               'Show Status', 'Add IP Exception', 'Rate Limiting', 'Logging Control'],
    'Windows_Command': [
        'Windows Defender Firewall with Advanced Security',
        'wf.msc or netsh advfirewall',
        'netsh advfirewall set allprofiles state on/off',
        'netsh advfirewall firewall show rule dir=in/out',
        'netsh advfirewall firewall add rule name="RuleName" dir=in action=allow protocol=TCP localport=PORT',
        'netsh advfirewall firewall add rule name="RuleName" dir=in action=block protocol=TCP localport=PORT',
        'netsh advfirewall firewall add rule name="RuleName" dir=in action=allow service=SERVICE',
        'netsh advfirewall firewall add rule name="RuleName" dir=in action=block service=SERVICE',
        'netsh advfirewall set allprofiles firewallpolicy blockinbound,allowoutbound',
        'netsh advfirewall firewall delete rule name="RuleName"',
        'netsh advfirewall reset',
        'netsh advfirewall show allprofiles',
        'netsh advfirewall firewall add rule name="RuleName" dir=in action=allow remoteip=IP',
        'Not directly available in basic firewall',
        'netsh advfirewall set allprofiles logging droplevel enable'
    ],
    'Linux_UFW_Command': [
        'UFW (Uncomplicated Firewall)',
        'sudo ufw or iptables directly',
        'sudo ufw enable/disable',
        'sudo ufw status numbered',
        'sudo ufw allow PORT/tcp',
        'sudo ufw deny PORT/tcp',
        'sudo ufw allow SERVICE',
        'sudo ufw deny SERVICE',
        'sudo ufw default deny incoming; sudo ufw default allow outgoing',
        'sudo ufw delete RULE_NUMBER',
        'sudo ufw --force reset',
        'sudo ufw status verbose',
        'sudo ufw allow from IP',
        'sudo ufw limit ssh',
        'sudo ufw logging on/off'
    ],
    'Complexity': ['Medium', 'Medium', 'Low', 'Low', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Low', 'Low',
                  'Low', 'Medium', 'High', 'Low'],
    'GUI_Available': ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes',
                     'Yes', 'Yes', 'No', 'Yes'],
    'Notes': [
        'Built into Windows, enterprise-grade features',
        'Multiple access methods available',
        'Can be managed via Group Policy',
        'Very detailed rule listing with filters',
        'Supports advanced rule conditions',
        'Supports advanced blocking conditions',
        'Can target specific Windows services',
        'Can block specific Windows services',
        'Granular control per profile (domain/private/public)',
        'Rule deletion by name or properties',
        'Complete firewall reset available',
        'Shows status per profile',
        'Supports IP ranges and subnets',
        'Advanced rate limiting requires 3rd party tools',
        'Comprehensive logging options',
    ]
}

df_comparison = pd.DataFrame(comparison_data)
df_comparison.to_csv('windows_vs_linux_firewall_comparison.csv', index=False)
print("Created windows_vs_linux_firewall_comparison.csv")

# Display a simplified view
simple_view = df_comparison[['Feature', 'Windows_Command', 'Linux_UFW_Command', 'Complexity']].head(10)
print("\nFirewall Command Comparison (First 10 entries):")
print(simple_view.to_string(index=False))