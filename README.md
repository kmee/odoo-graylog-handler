# graylog2_handler
GrayLog2 handler for Odoo

Provides ability to send log messages to graylog2 server

### Clone repository
git clone https://github.com/kmee/graylog2_handler.git

### Setup odoo
Edit odoo.cfg file and add these values

* add full path of graylog2_handler to addons_path

and add gelf options

* gelf_enabled=True
* gelf_host=[Graylog2 IP_ADDRESS or FQDN]
* gelf_port=[Graylog2 Stream Port]
* gelf_localname=LOCAL_MACHINE_NAME

Save, restart odoo
### Install module
* Join on odoo
* update module list
* install GrayLog2 Handler module (graylog2_handler)
