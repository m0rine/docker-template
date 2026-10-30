#!/usr/bin/env bash
set -Eeuo pipefail
echo "This script assumes you're already logged into dockerhub, and asks the username for tagging."
echo "Set the DOCKER_USER environment variable to avoid having to manually input each time."
# Configuration
DOCKER_USER="${DOCKER_USER:-$(read -rp 'DockerHub username: ' USERNAME && echo "$USERNAME")}"
PREFIX="docker.io/${DOCKER_USER}/template"
POSTFIX="$(git log --format=%H -1)"
MODE="${1:-all}"

usage() {
    echo "Usage: $0 [all|build|push]"
    exit 1
}

case "$MODE" in
    all|build|push) ;;
    *) usage ;;
esac

IMAGES=("frontend:prod" "middleware:prod" "database:")

build_image() {
    local NAME="$1"
    local TARGET="$2"
    local TAGS=(-t "$PREFIX:$NAME-$POSTFIX" -t "$PREFIX:$NAME-latest")

    echo "Building $NAME..."

    local ARGS=(docker buildx build "${TAGS[@]}")
    [[ -n "$TARGET" ]] && ARGS+=(--target "$TARGET")
    ARGS+=("./$NAME")

    "${ARGS[@]}"
}

push_image() {
    local NAME="$1"

    echo "Pushing $NAME..."
    docker push "$PREFIX:$NAME-$POSTFIX"
    docker push "$PREFIX:$NAME-latest"
}

for IMAGE in "${IMAGES[@]}"; do
    NAME="${IMAGE%%:*}"
    TARGET="${IMAGE#*:}"

    [[ "$MODE" != "push" ]] && build_image "$NAME" "$TARGET"
    [[ "$MODE" != "build" ]] && push_image "$NAME"
done

echo "Completed successfully! ($MODE)"
echo "Commit: $POSTFIX"
