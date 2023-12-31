# ETL Web to GCS

This Python script defines an ETL (Extract, Transform, Load) workflow using Prefect to fetch data from the web, clean it, and load it into Google Cloud Storage (GCS). The script is designed to work with taxi trip data but can be adapted for other datasets.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Setting up Prefect](#setting-up-prefect)
  - [Running the ETL](#running-the-etl)
- [Workflow Explanation](#workflow-explanation)
  - [Tasks](#tasks)
- [Docker Support](#docker-support)
- [Contributing](#contributing)
- [License](#license)

## Overview

The script defines an ETL workflow that consists of the following steps:

1. **Fetch**: It fetches taxi trip data from a specified URL and loads it into a Pandas DataFrame.

2. **Clean**: This task cleans the data, converting datetime columns to the correct data type and prints some basic statistics.

3. **Write Local**: It writes the cleaned data as a Parquet file locally.

4. **Write GCS**: This task uploads the local Parquet file to Google Cloud Storage (GCS).

## Prerequisites

Before running the ETL workflow, ensure you have the following prerequisites installed and configured:

- Python (3.7+)
- [Prefect](https://docs.prefect.io/core/getting_started/installation.html)
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
- Access to a Google Cloud Storage bucket

## Getting Started

### Setting up Prefect

1. Install Prefect:

   ```bash
   pip install prefect
   ```

2. Configure Prefect (follow the official Prefect documentation for setup).

3. Create a Prefect project and set up your credentials.

### Running the ETL

1. Clone this repository.

2. Navigate to the project directory:

   ```bash
   cd etl-web-to-gcs
   ```

3. Run the ETL script:

   ```bash
   python etl_web_to_gcs.py
   ```

## Workflow Explanation

### Tasks

- **Fetch**: This task uses `pd.read_csv` to fetch data from the specified URL. It retries up to 3 times and caches results for 1 day to reduce redundant requests.

- **Clean**: This task fixes data type issues in the DataFrame, converting datetime columns to the correct data type. It also prints basic statistics about the cleaned data.

- **Write Local**: This task writes the cleaned DataFrame as a Parquet file locally.

- **Write GCS**: This task uploads the local Parquet file to a specified path in Google Cloud Storage.

## Docker Support

This project includes a Dockerfile and Docker requirements for containerization. To use Docker, follow the instructions in the `docker_deploy.py` script to build and deploy the ETL workflow as a Docker container.

## Contributing

Contributions to this project are welcome. If you'd like to contribute, please follow the standard GitHub workflow: fork the repository, create a branch, make changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute it as per the terms of the license.

Enjoy working with your ETL Web to GCS workflow!
```
