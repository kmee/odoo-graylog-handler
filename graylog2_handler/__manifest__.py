{
    "name": "GrayLog2 Handler",
    "version": "14.0.1.0.0",
    "author": "Management adn Accounting On-line",
    "summary": "Provides ability to send log messages to graylog2 server",
    "depends": [
    ],
    "description": """
Aditional options available for config file:
    gelf_enabled: bool
    gelf_host: string, required if gelf_enabled=True
    gelf_port: integer, required if gelf_enabled=True
    gelf_localname: string

    """,
    "license": "LGPL-3",
    "external_dependencies": {
        "python": ["graypy"]
    },
    "active": True,
}
