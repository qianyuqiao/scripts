curl -R -O http://www.lua.org/ftp/lua-5.3.4.tar.gz
tar zxf lua-5.3.4.tar.gz
cd lua-5.3.4
sudo make linux test
apt-get install libreadline-dev -y # if error in the last step
sudo make linux test
make install
locate lua
