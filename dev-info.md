Python Package 
--------------

Use of python2.7

1) Installation needed packages
apt-get install python-pip
pip2 install --upgrade pip
python -m pip list
python -m pip install setuptools wheel twine


2) Generate two files in the dist directory
python setup.py sdist bdist_wheel


3) Uploading the distribution archives
Go to dir where setup.py is located
twine upload dist/*


5) Test: Installing your newly uploaded package
[python -m pip install bcwalletx]
pip install bcwalletx

OUTPUT
...
Installing collected packages: bcwalletx, requests
  Found existing installation: requests 2.19.1
    Uninstalling requests-2.19.1:
      Successfully uninstalled requests-2.19.1
Successfully installed bcwalletx-1.2.9 requests-2.4.3


6) Deinstallation
pip uninstall bcwalletx
rm -rf bcwalletx.egg-info build dist
pip3 uninstall requests
pip3 install requests
