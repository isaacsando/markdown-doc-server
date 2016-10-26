Distro Install Packages
----------------
- sane-utils
- libtiff-tools
- lsb
- cups
- xsltproc
- samba (for accessing share from Windows)
- libpam-smbpass
- imagemagick (for mogrify)

Epson Packages
--------------
Go to the [Epson Site](http://download.ebz.epson.net/dsc/search/01/search/?OSC=LX)
and do a search for **Epson Workforce 545**. Install the following packages *in
the order listed*:

1. epson-inkjet-printer-201106w_1.0.1-1lsb3.2_i386.deb
2. iscan-data_1.14.0-1_all.deb
3. iscan_2.28.1-3.**ltdl7**_i386.deb (*not* ltdl3)
4. iscan-network-nt_1.1.0-2_i386.deb

/etc/sane.d/epkowa.conf:
---------------------------------------------
```
net 192.168.1.8
```

/etc/sane.d/epson2.conf:
-------------------------------------------------------
```
# net autodiscovery
```

/etc/samba/smb.conf:
----------------------------
```
[scans]
path = "/home/isaac/scans"
```
