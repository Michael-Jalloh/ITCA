# Auth

This is a authentication package, that will help in facilitating a centralize authentication scheme for different sites.

## Installation

cd into the directory

`cd ITCA`
 
then type 

`sudo apt install virtualenv`

then next type
 
`virtualenv .` to install to current directory

then type

`pip install -r requirements.txt`
 
if you encounter permission denied then type

`pip install -r requirements.txt`

## Usage
`python app.py`

The expose urls are below and are post methods

`/api/v1/sign-up`

`/api/v1/verify`

The signup url expects
  * username
  * first_name
  * last_name
  * email
  * password

The verify url expects
  * email
  * password
