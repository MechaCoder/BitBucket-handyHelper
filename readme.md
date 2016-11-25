# Handy helper for pipelines

This is a toold for runing some commands in when you are useing bit bucket's piplines to test and deploy, i went with idea that a devopement will want to run some commands but not outhers, an exsample of commands that you don't want to run is the insterlation of dependecys or hiting an outside service. The basic idea that a devoper should be able to run testing and code complince tools with in there local envoiment.

## useage
you can this script in two ways the first is self run the self running runs with a defult seting to run python commands amd PEP8 commands
the secound was is to use the script in anuther script you can do this by importing script into a version control (svn, git or hg) hook.

## geting started
1. you need to install the dependecy you can do this by uesing `requirements-hh.txt` (useing the pip command `pip install -r requirements-hh.txt`) or by installing the dependecy `yamlcfg`,
2. this tool is designed to placed as a file on the root of the project and this and there also needs `bitbucket-pipeline.yml` that works
