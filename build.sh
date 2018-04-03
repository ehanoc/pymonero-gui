#!/bin/sh

ROOT_FOLDER=${PWD}
echo $ROOT_FOLDER

cd pymonero
make

cd build/release/src/wallet/api
make install

echo "ready!"
