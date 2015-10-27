#!/bin/bash
# Creates a tar ball and, if on the master branch, will also create a tag.
export PATH=$PATH:/usr/local/bin

DATE=$(date +"%Y-%m-%d_%H-%M-%S")
BRANCH=$(git symbolic-ref --short -q HEAD)
VERSION=$(grep "^VERSION = ('[0-9+]', '[0-9+]', '[0-9+]')$" ./holding_page/__init__.py | sed s/"VERSION = ('"//g | sed s/","/"."/g | sed s/"'"//g | sed s/" "//g | sed s/")"//g)
PACKAGE_NAME=$(grep "name='[a-z\-]*',$" ./setup.py | sed s/"name='"//g | sed s/"',"//g | sed s/" "//g)


if [ "$BRANCH" == "master" ]; then
    git tag $VERSION\_$DATE -m "Automatically tagging release"
fi

FILE_NAME="$PACKAGE_NAME-$VERSION.tar.gz"

python setup.py sdist upload
echo "Created ${FILE_NAME}"
