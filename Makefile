default:
	quarto preview

docs:
	quarto render

test:
	npm run --silent ajv -- compile -s schema.json
	npm run --silent validate example-1.json
	npm run --silent validate example-2.json
	npm run --silent validate example-4.json
	npm run --silent validate fq-1.json
	npm run --silent validate fq-2.json
	npm run --silent validate nested-example-1.json
	npm run --silent validate nested-example-2.json
	npm run --silent validate nested-report-1.json
