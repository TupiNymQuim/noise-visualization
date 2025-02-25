#!/bin/bash

tshark -i enp6s0 -T fields -e frame.len -q -a duration:1
