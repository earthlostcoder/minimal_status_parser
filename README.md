minimal_status_parser
=====================

Parses the Earthlost Status Page, and persists the Shipcount

Readme for Debian Users, Linux Users can adopt this easy. Windows and Mac Users may use google on how to set up Python and the Requirements

Requirements:

Python2.6 or Python2.7

lxml:

  install with
  
    pip install lxml

  - needs libxslt-dev
  - needs libxml2-dev
  - needs python-dev

or install with 
  
    apt-get install python-lxml

  - handles the requirements

sqlite3:

    apt-get install sqlite3
    
  - So you can check the database and make your queries ;-)
  

Startup:

    python check_status.py
