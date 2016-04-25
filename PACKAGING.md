Packaging
=========

Currently there is only debian package, it is packaged with dh-virtualenv,
see https://dh-virtualenv.readthedocs.org/en/latest/

Once you have build-essential, debhelper and dh-virtualenv install it
is a matter of executing the following command to get a debian package

    dpkg-buildpackage -us -uc
