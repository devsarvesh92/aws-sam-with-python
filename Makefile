define setup
	@pdm export --without-hashes -o requirements.txt
endef

define download-encryption-keys
	aws s3 cp s3://sam-encryption-bucket/ . --recursive --profile personal; 
endef

download-encryption-keys:
	@echo -e "Downloading encryption keys..."
	$(call download-encryption-keys)

setup: download-encryption-keys
	$(call setup, "setup completed!")