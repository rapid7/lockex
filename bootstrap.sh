#!/bin/bash

sudo apt-get -y update || exit 1
sudo apt-get -y install devscripts python-virtualenv git equivs python-dev || exit 1
rm -rf dh-virtualenv
(git clone https://github.com/spotify/dh-virtualenv.git && \
    cd dh-virtualenv && \
    sudo bash -c 'yes | mk-build-deps -ri' && \
    dpkg-buildpackage -us -uc -b) || exit 1
sudo dpkg -i dh-virtualenv_*_all.deb || exit 1

cd build && mkdir -p build/pkg && git archive --format tar HEAD | tar -vx -C build/pkg/ || exit 1
cd build/pkg && dpkg-buildpackage -us -uc
