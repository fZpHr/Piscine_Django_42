#!/bin/sh

curl -sIL $1 | grep location -n | grep 18 | cut -d' ' -f2