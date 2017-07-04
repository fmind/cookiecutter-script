#!/bin/sh

chmod u+x {{cookiecutter.script}}.py
mv {{cookiecutter.script}}.py ../

cd ..; rm -r {{cookiecutter.script}}
