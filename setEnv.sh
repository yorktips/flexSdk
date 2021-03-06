#!/bin/bash
###############################################################################
#
# THIS SCRIPT IS USED TO CREATE OPENSNAPROUTE RUNNING/BUILDING ENVIRONMENT
# Auther:   York Chen
# Date:     2017-01-05
# Usage:    opx_installer.sh 
# Example:  opx_installer.sh 
#
###############################################################################
whoami=$(whoami)
if [ ! "$whoami" == "root" ]; then
  echo "You are $whoami. Please run this script with root"
  exit
else
  echo "you are root"
fi
mypath=$(pwd)

apt-get update
apt-get -y upgrade

#[TODO: this list is out of date as of 2013-07]
#  automake:       1.9.6 (released 2005-07-10)
#  autoconf:       2.59 (2.60 on 2006-06-26 is too recent to require)
#  libtool:        1.5.22 (released 2005-12-18)
#  texinfo:        4.7 (released 2004-04-10; 4.8 is not yet common)
#  GNU AWK:        3.1.5 (released 2005-08-12)

#Check automake installation
which_automake=$(which automake)
if [ "$which_automake" == "" ]; then
	#install automake
	apt-get -y install automake
fi

#Check autoconf installation
which_autoconf=$(which autoconf)
if [ "$which_autoconf" == "" ]; then
	#install autotools-dev	
	apt-get -y install autotools-dev
	
	#install autoconf
	apt-get -y install autoconf
fi

#Check libtool installation
which_libtool=$(which libtool)
if [ "$which_libtool" == "" ]; then
	#install libtoo
	apt-get -y install libtool-bin
fi

#Check texinfo installation
if [ ! -d "/usr/lib/texinfo" ]; then
	apt-get -y install texinfo
fi

#Check gawk installation
which_gawk=$(which gawk)
if [ "$which_gawk" == "" ]; then
	#install gawk
	apt-get -y install gawk
fi

#Check libreadline	installation			
if [ ! -d "/usr/share/doc/libreadline6" ]; then
	apt-get -y install libreadline6 libreadline6-dev
fi

#Check git installation
which_git=$(which git)
if [ "$which_git" == "" ]; then
	#install git
	apt-get -y install git
fi

#Check diffstat	installation
if [ ! -f "/usr/bin/diffstat" ]; then
	apt-get -y install diffstat
fi


#Check unzip installation
if [ -f "/usr/bin/unzip" ]; then
	apt-get -y install unzip
fi

#Check gcc-multilib installation
if [ -f "/var/lib/dpkg/info/gcc-multilib.list" ]; then
	apt-get -y install gcc-multilib
fi


#Check build-essential installation
if [ -d "/usr/share/build-essential" ]; then
	apt-get -y install build-essential
fi


#chrpath
if [ ! -f "/var/lib/dpkg/info/chrpath.list" ]; then
	apt-get -y install chrpath
fi

#Check screen installation
which_screen=$(which screen)
if [ "$which_screen" == "" ]; then
	#install screen
	apt-get -y install screen
fi

#Check curl installation
which_curl=$(which curl)
if [ "$which_curl" == "" ]; then
	#install curl
	apt-get -y install curl
fi


#Check xterm installation
which_xterm=$(which xterm)
if [ "$which_xterm" == "" ]; then
	#install xterm
	apt-get -y install xterm
fi


#Checkdevice-tree-compiler installation
if [ ! -d "/usr/share/doc/device-tree-compiler" ]; then
	apt-get -y install device-tree-compiler
fi


#Check libsdl1.2-dev installation
if [ ! -d "/usr/share/doc/libsdl1.2-dev" ]; then
	apt-get -y install libsdl1.2-dev
fi


#Check thrift installation
which_thrift=$(which thrift)
if [ "$which_thrift" == "" ]; then
	#install thrift-compiler
	apt-get -y install thrift-compiler
fi


#Check byacc installation
which_vagrant=$(which vagrant)
if [ "$which_vagrant" == "" ]; then
	#install vagrant
	apt-get -y install vagrant
fi


#Check flex installation
which_flex=$(which flex)
if [ "$which_flex" == "" ]; then
	#install flex
	apt-get -y install flex
fi


#Check byacc installation
which_yacc=$(which yacc)
if [ "$which_yacc" == "" ]; then
	#install byacc
	apt-get -y install byacc
fi


#Check bison installation
which_bison=$(which bison)
if [ "$which_bison" == "" ]; then
	#install bison
	apt-get -y install bison
fi

#
#Update package information, ensure that APT works with the https method, and 
#that CA certificates are installed.
#
#apt-get install apt-transport-https ca-certificates

#Add the new GPG key
#               --keyserver hkp://ha.pool.sks-keyservers.net:80 \
#               --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
			   
#Check docker installation
which_docker=$(which docker)
if [ "$which_docker" == "" ]; then

	apt-get -y install apt-utils
	#install docker
	apt-get install -y docker.io
	systemctl start docker
	systemctl enable docker
	
	docker_server_version=$(docker version | awk 'BEGIN{found=0;}{if ($1=="Server:") found=1; if (found==1){if ($1=="Version:") {print $2;}}}')
	if [ "$docker_server_version" == "" ]; then
		echo "Error: Failed to install docker"
		exit
	else
		echo "Docker server version:$docker_server_version"
	fi
fi

	
if [ ! -d "/etc/systemd/system/docker.service.d" ]; then
	mkdir -p "/etc/systemd/system/docker.service.d"
fi

http_proxy_conf="/etc/systemd/system/docker.service.d/http-proxy.conf"

if [ ! -f "$http_proxy_conf" ]; then
	echo "[Service]" > "$http_proxy_conf"
	echo "Environment=\"NO_PROXY=68.232.67.139\"" >> "$http_proxy_conf"
	systemctl daemon-reload
fi

environment_docker=$(systemctl show --property Environment docker |awk 'BEGIN{FS="=";}{ print $2;}')
if [ "$environment_docker" == "NO_PROXY" ]; then	
	systemctl show --property Environment docker
else
	echo "Http proxy wrong"
	exit
fi

#restart docker
systemctl restart docker

#Get FlexSwitch docker image	 
snapos_docker_repos=$(docker search snapos | sed -n 2p | awk '{print $1;}')
if [ "$snapos_docker_repos" == "" ]; then
	echo "Error: Failed to get flexswitch docker repository"
	exit
else
	echo "Flexswitch docker repository is $snapos_docker_repos"
fi


if [ ! -d "$mypath/projects" ]; then
        mkdir "$mypath/projects"
fi

cd $mypath/projects


if [ ! -d "$mypath/projects/test" ]; then
	git clone  https://github.com/OpenSnaproute/test
fi


if [ ! -f "$mypath/projects/test/docker_startup.sh" ]; then
	echo "Error: Failed to get https://github.com/OpenSnaproute/test"
	exit
else
	cd $mypath/projects/test
	./docker_kill.sh	
	./docker_startup.sh
	
	d_inst1=$(docker ps | grep d_inst1 | awk '{print $1}')
	
	if [ "$d_inst1" == "" ]; then
		echo "Docker container failed"
		exit
	else
		echo "Run following commands to start flexswitch"
		echo "docker exec -i -t $d_inst1"
		echo "service flexswitch restart"
	fi
fi


#Create docker container
#docker run --privileged -v /tmp:/tmp -v /dev/log:/dev/log -v /sys/fs/cgroup:/sys/fs/cgroup -h ops1 --name ops1 joeneville/ops /sbin/init &



