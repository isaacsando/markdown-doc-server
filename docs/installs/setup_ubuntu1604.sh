``` bash
#!/bin/bash

if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root" 1>&2
    exit 1
fi

function install_wine() {
    echo "[*] Installing wine..."
    dpkg --add-architecture i386
    add-apt-repository ppa:wine/wine-builds
    apt-get update -y
    apt-get install -y --install-recommends winehq-devel cabextract

    echo "[*] Installing winetricks..."
    wget  https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks
    chmod +x winetricks
    echo "[!] Do not install Mono"
    winecfg
    sh winetricks vcrun6 vcrun6sp6 dotnet4
}

apt-get update
apt-get install -y \
    git rsync vim guake tmux wget spice-vdagent xserver-xorg-video-qxl \
    openssh-server
apt-get upgrade -y

systemctl enable ssh
systemctl start ssh

while true
do read -p "Install wine? (Y/n): "
    case "$REPLY" in 
        y|Y|"")   install_wine 
                  break;;
        n|N)      break;; 
        *)        echo "Please enter y/n";;
    esac
done

echo "[*] Also copy over .vim and .vimrc!"
```
