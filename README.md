# graylog2_handler
GrayLog2 handler for Odoo

Edit odoo.cfg and add these values

gelf_enabled=True
gelf_host=[Graylog2 IP_ADDRESS or FQDN]
gelf_port=[Graylog2 Stream Port]
gelf_localname=LOCAL_MACHINE_NAME

Save, restart odoo, update module list and install GrayLog2 Handler module (graylog2_handler)
