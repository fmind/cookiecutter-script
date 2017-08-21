#!/bin/sh

chmod u+x {{cookiecutter.script}}.py
mv {{cookiecutter.script}}.py ../

cd ..; rmdir {{cookiecutter.script}}
