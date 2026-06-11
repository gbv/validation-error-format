default:
	quarto preview

docs:
	quarto render

test:
	@npm run --silent ajv -- compile -s schema.json
	@npm run --silent validate examples/example-1.json
	@npm run --silent validate examples/example-2.json
	@npm run --silent validate examples/example-4.json
	@npm run --silent validate examples/fq-1.json
	@npm run --silent validate examples/fq-2.json
	@npm run --silent validate examples/nested-example-1.json
	@npm run --silent validate examples/nested-example-2.json
	@npm run --silent validate examples/nested-report-1.json
