#!/bin/bash

source .env

trap 'handler $? $LINENO' ERR

handler() {
    printf "%b" "${FAIL} ✗ ${NC}sia entry failed with exit status $1 on line $2\n"
}

usage() {
  cat <<EOF
Usage: ./sia.sh -s [ --samples ] -r [ --range ]
       ./sia.sh # run defaults
 
Arguments:
[ -s ]      sample size / agent population
[ -r ]      integer range from [ 0,X ]
EOF
}

PARAMS=""

while (( "$#" )); do
  case "$1" in
    -s|--samples)
      SAMPLES="$2"
      shift
      ;;
    -r|--range)
      RANGE="$2"
      shift
      ;;
    -*|--*=) # unsupported flags
      echo "Error: Unsupported flag $1" >&2
      printf "%b" "$(usage)\n"
      exit 1
      ;;
    *) # preserve positional arguments
      PARAMS="$PARAMS $1"
      shift
      ;;
  esac
done
# set positional arguments in their proper place
eval set -- "$PARAMS"

printf "%b" "${OKB}Swarm Intelligent Agents Demo\n
=============================\n
Copyright © 2021 LEAP Systems. All Rights Reserved.\n${NC}"

python3 -m sia "$SAMPLES" "$RANGE"