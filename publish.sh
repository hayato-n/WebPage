# !/bin/sh
make publish
ghp-import output
git push -f origin gh-pages:master