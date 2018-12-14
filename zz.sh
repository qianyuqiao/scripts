#!/bin/sh
pip install selenium
url="https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2"
wget  "${url}"
binary="phantomjs-2.1.1-linux-x86_64.tar.bz2"
tar -xvf ${binary}
cp   ./phantomjs-2.1.1-linux-x86_64/bin/phantomjs   /usr/bin/phantomjs
wget https://raw.githubusercontent.com/qianyuqiao/scripts/master/access.py
python access.py
