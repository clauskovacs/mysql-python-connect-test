# mysql-python-connect-test
A small (test)program to demonstate/test the connection to a SQL database using the *mysql.connector* in python.

## Description
This python program connects to a SQL database and lists all databases.

## Dependencies
The python package **mysql-connector-python** is needed, which can be installed using pip3 via `pip3 install mysql-connector`

Additionally, all installed python packages as well as all installed linux packages are provided for debugging purposes (see */info*). The operating system used was Fedora30 (5.6.13-100.fc30.x86_64).

## Running the program
The following must be done to run the program:

1. Set the login credentials in */src/config.py*
2. Run the program using **python3 src/pySQLconnectTest.py**
