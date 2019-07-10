MADGRAPH_VERSION=$1
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
TAG="recast/madgraph-pythia:v$MADGRAPH_VERSION"

echo "$DOCKER_PASSWORD" | docker login --username $DOCKER_USERNAME --password-stdin
echo "MADGRAPH_VERSION is ${MADGRAPH_VERSION}"
docker build -t $TAG --build-arg MADGRAPH_VERSION=$MADGRAPH_VERSION $DIR
docker push $TAG
docker images
