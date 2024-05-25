#!/bin/sh

if [ ! -f $json_file ]; then
    echo "[" > $json_file
else
    sed -i s/']'/','/g $json_file
fi

