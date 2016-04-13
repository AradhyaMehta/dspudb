The following are the instructions that need to be followed for running the application smoothly. All of the steps excluding step 1 and 2 have to be carried out in command prompt.

1) Install MySQL installer/workbench.
	  Task: Open MySql and create an empty schema called 'application'. Don't add any tables or entries since that will be done when our     zip files are used.
2) Install python v2.7.7
3) Install 'pip' from pip.readtheorgs.org/en/latest/installing.html
4) Create a virtual environment.
	  Command: pip install virtualenv
5) Change the path to desktop using 'cd desktop'
6) Create a virtual environment folder abc in desktop
	  Command: virtualenv abc
7) Install django v1.9.5 using the command 'pip install django'
8) Activate the virtual environment abc
	  Command: .\Scripts\activate
9) Install multiple packages once inside the virtual environment.
	  Command: pip install django-auditlog
	  Command: pip install django-fernet-fields
	  Command: pip install six
	  Command: pip install mysqlclient
10) Start a project inside the environment.
	  Command: python .\Scripts\django-admin.py startproject dspudb
	  Then rename the folder 'dspudb' as 'src'
11) Start an app inside the environment
	  Command: python manage.py startapp udbapp
12) Copy the following files from the zip folder to the corresponding location under the dspudb folder:
	  - dspudb/urls.py
	  - The complete template folder
	  - Replace all the files from the udbapp folder with the files from the corresponding udbapp folder in the zip file.
13) Edit the setting.py file according to the instructions given in edit_settingspy.txt
14) Extract all the files from our zip file and extract it to the 'abc' folder
15) Once these packages have been downloaded, move to the src folder inside 'abc' using 'cd src'
16) Once inside src, run the manage.py file.
	  Command: python manage.py makemigrations
	  Command: python manage.py migrate
	  Command: python manage.py runserver
