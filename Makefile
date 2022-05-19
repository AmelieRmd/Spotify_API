
# - - - - - - - - - - - - - - - - - - - - - - - - -
# model

train:
	python -m trainer.trainer  # if the provided model.joblib does not load

# - - - - - - - - - - - - - - - - - - - - - - - - -
# api 🤖

run_api:
	uvicorn api.fast:app --reload

# - - - - - - - - - - - - - - - - - - - - - - - - -
# docker 🐳
# 🚨 1. set your correct project id in GCP_PROJECT_ID

GCP_PROJECT_ID=dogwood-dryad-337815
DOCKER_IMAGE_NAME=data-certification
GCR_MULTI_REGION=eu.gcr.io
GCR_REGION=europe-west1

docker_params:
	@echo "project id: ${GCP_PROJECT_ID}"
	@echo "image name: ${DOCKER_IMAGE_NAME}"
	@echo "multi region: ${GCR_MULTI_REGION}"
	@echo "region: ${GCR_REGION}"

docker_build:
	docker build -t ${GCR_MULTI_REGION}/${GCP_PROJECT_ID}/${DOCKER_IMAGE_NAME} .

docker_run:
	docker run -e PORT=8000 -p 8000:8000 ${GCR_MULTI_REGION}/${GCP_PROJECT_ID}/${DOCKER_IMAGE_NAME}

docker_push:
	docker push ${GCR_MULTI_REGION}/${GCP_PROJECT_ID}/${DOCKER_IMAGE_NAME}

docker_deploy:
	gcloud run deploy --image ${GCR_MULTI_REGION}/${GCP_PROJECT_ID}/${DOCKER_IMAGE_NAME} --platform managed --region ${GCR_REGION}
