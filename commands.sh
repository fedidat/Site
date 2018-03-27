#Not working for some reason
git push -f git@github.com:fedidat/fedidat.github.io.git gh-pages:master
ghp-import .

#First test the site
cd output; python -m pelican.server
#Come back and generate output
cd ..; pelican content -o output -s pelicanconf.py

#Commit this repo
git add -A; git commit -m "article"; git push
#Commit the site
cp /home/ben/Desktop/dev/Site/output/* /home/ben/Desktop/dev/fedidat.github.io/; git add -A; git commit -m "article"; git push
