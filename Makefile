all: build

build:
	node_modules/typescript/bin/tsc --target ES5 navigation_transitions.ts

.PHONY: build
