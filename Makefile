load:
	bin/molotov --workers 10 --processes 4

github:
	bin/moloslave https://github.com/tarekziade/molodemo big

docker:
	docker run -e TEST_REPO=https://github.com/tarekziade/molodemo -e TEST_NAME=big tarekziade/molotov:latest


