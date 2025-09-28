# Create a horizontal timeline flowchart for the firewall configuration project
diagram_code = """
flowchart LR
    A[1. Open FW Tool<br/>5 min] --> B[2. List Rules<br/>10 min]
    B --> C[3. Block Port 23<br/>15 min]
    C --> D[4. Test Block<br/>10 min]
    D --> E[5. Allow SSH<br/>15 min]
    E --> F[6. Remove Test<br/>10 min]
    F --> G[7. Document<br/>20 min]
    G --> H[8. Analyze Filter<br/>15 min]
    
    classDef stepBox fill:#B3E5EC,stroke:#1FB8CD,stroke-width:2px
    class A,B,C,D,E,F,G,H stepBox
"""

# Create the mermaid diagram and save as both PNG and SVG
png_path, svg_path = create_mermaid_diagram(diagram_code, 'firewall_timeline.png', 'firewall_timeline.svg')

print(f"Timeline chart saved as: {png_path} and {svg_path}")