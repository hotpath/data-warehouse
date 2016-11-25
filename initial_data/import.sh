#!/bin/bash

cat DATASET.csv | \
	docker exec -i datasource_mongo_1 \
		mongoimport --drop --type csv --headerline --db cein --collection dataset

