VERSION := $(shell git describe --abbrev=0 --tags)
BUILD_DATE := "$(shell date -u)"
VCS_REF := $(shell git log -1 --pretty=%h)
NAME := $(shell pwd | xargs basename)
VENDOR := "Matt Hodges"
ORG := hodgesmr
WORKDIR := "/opt/2020_map/"

print:
	@echo BUILD_DATE=${BUILD_DATE}
	@echo NAME=${NAME}
	@echo ORG=${ORG}
	@echo VCS_REF=${VCS_REF}
	@echo VENDOR=${VENDOR}
	@echo VERSION=${VERSION}
	@echo WORKDIR=${WORKDIR}

.EXPORT_ALL_VARIABLES:
build:
	docker build \
	-f Dockerfile \
	-t ${ORG}/${NAME}:${VERSION} \
	-t ${ORG}/${NAME}:latest . \
	--build-arg VERSION=${VERSION} \
	--build-arg BUILD_DATE=${BUILD_DATE} \
	--build-arg VCS_REF=${VCS_REF} \
	--build-arg NAME=${NAME} \
	--build-arg VENDOR=${VENDOR} \
	--build-arg ORG=${ORG} \
	--build-arg WORKDIR=${WORKDIR}

.EXPORT_ALL_VARIABLES:
map:
	docker run --rm -v "$(PWD)/output:${WORKDIR}/output" ${ORG}/${NAME}
