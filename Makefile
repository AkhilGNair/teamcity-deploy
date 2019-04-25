build:
	docker-compose build
	docker-compose push

deploy:
	kubectl delete --ignore-not-found=true -f pod.yaml
	kubectl apply -f pod.yaml

run:
	make build
	make deploy
