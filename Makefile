UNAME := $(shell uname)
ARCH_NAME := $(shell uname -m)
YQ_VERSION=v4.27.2
BASE_PATH :=$(shell pwd)
ifeq ($(UNAME), Darwin)
ifeq ($(ARCH_NAME), x86_64)
OS=darwin
CHIPSET=amd64
else
OS=linux
endif
endif

install:
	mv ${BASE_PATH}/plugin/kubectl-shark /usr/local/bin/