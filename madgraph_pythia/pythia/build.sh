PYTHIA_VERSION=$1
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
TAG="recast/pythia:$PYTHIA_VERSION"

echo "$DOCKER_PASSWORD" | docker login --username $DOCKER_USERNAME --password-stdin
echo "PYTHIA_VERSION is ${PYTHIA_VERSION}"
docker build -t $TAG --build-arg PYTHIA_VERSION=$PYTHIA_VERSION $DIR
docker push $TAG
docker images
