#!/bin/bash

tshark -i $1 -T fields -e frame.len -q -a duration:1
