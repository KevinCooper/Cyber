#!/bin/bash

#install the basics
sudo apt-get -y install vim
sudo apt-get -y install terminator
sudo apt-get -y install git
sudo apt-get -y install python-pip
sudo apt-get -y install python3-pip
sudo apt-get -y install python-dev
sudo apt-get -y install virtualenvwrapper
sudo apt-get -y install libxml2-dev
sudo apt-get -y install libxslt1-dev
sudo apt-get -y install libffi-dev
sudo apt-get -y install libreadline-dev
sudo apt-get -y install virtualenvwrapper python2.7-dev build-essential libxml2-dev libxslt1-dev git libffi-dev cmake libreadline-dev
sudo apt-get -y install python-dev libffi-dev build-essential virtualenvwrapper

sudo pip install virtualenvwrapper
sudo pip3 install virtualenvwrapper
#Get a good colorscheme for terminator
mkdir -p ~/.config/terminator/
git clone https://github.com/alinmindroc/Zenburn-for-Terminator
cp Zenburn-for-Terminator/config ~/.config/terminator/

mkdir ~/Desktop
cd ~/Desktop

mkdir binaries
mkdir web
mkdir forensics

pip install pwntools

#Get pwndbg
cd ~
pip install pycparser
pip3 install pycparser
git clone https://github.com/aquynh/capstone
cd capstone
./make.sh
sudo ./make.sh install
cd bindings/python
sudo python2 setup.py install # Ubuntu 12.04, GDB uses Python2
sudo python3 setup.py install # Ubuntu 14.04+, GDB uses Python3
cd ~
git clone https://github.com/zachriggle/pwndbg
echo "source $PWD/pwndbg/gdbinit.py" >> ~/.gdbinit

#Get rp++
# 64bit test
if [[ $(uname -m) == 'x86_64' ]];
then
  BIN="rp-lin-x64" 
else
  BIN="rp-lin-x86" 
fi
wget https://github.com/downloads/0vercl0k/rp/$BIN
mv $BIN rp++
chmod 755 rp++
mv rp++ ~/Desktop/binaries

cd ~
#install binwalk
git clone --depth 1 https://github.com/devttys0/binwalk.git
pip install -e binwalk
#install foremost
apt-get -y install foremost
#install z3
git clone https://github.com/Z3Prover/z3
cd z3
python scripts/mk_make.py
cd build
make
sudo make install


#Install angr
source "/usr/share/virtualenvwrapper/virtualenvwrapper.sh"
git clone --depth 1 https://github.com/angr/angr-dev
cd angr-dev
mkvirtualenv angr
./setup.sh
deactivate

#Get PIN
wget http://software.intel.com/sites/landingpage/pintool/downloads/pin-2.14-71313-gcc.4.4.7-linux.tar.gz -O pin.tar.gz
tar -xf pin.tar.gz
mv pin-2.14-71313-gcc.4.4.7-linux/ pin/
rm pin.tar.gz

#Install Triton - github
sudo apt-get -y install libboost-all-dev
git clone https://github.com/JonathanSalwan/Triton.git
cd Triton
mkdir build
cd build
cmake ..
make
sudo make install
cd ..
sudo python ./setup.py install

#Install Triton with PIN
cd pin/source/tools/
git clone https://github.com/JonathanSalwan/Triton.git
cd Triton
mkdir build
cd build
cmake -DPINTOOL=yes ..
make
cd ..
echo "./triton ./src/examples/pin/ir.py /usr/bin/id" > EXAMPLE.txt
cd ../../../../
rm -rf Triton
ln -s pin/source/tools/Triton TritonWithPin
