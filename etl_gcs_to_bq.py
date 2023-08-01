from pathlib import Path
import pandas as pd
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp.cloud_storage import GcpCredentials 

@task(retries=3,log_prints=True)
def extract_from_gcs(color:str, year:int, month:int):
    """Download data from GCS"""
    gcs_path= f"data\{color}\{color}_tripdata_{year}-{month:02}.parquet"
    gcp_block = GcsBucket.load("prefect-gcs-1")
    gcp_block.get_directory(from_path=gcs_path, local_path=f"")
    print(gcs_path)
    return Path(f"../data/{gcs_path}")
@task()
def transform(path: Path) -> pd.DataFrame:
    """ Data cleaning """
    df = pd.read_parquet(path)
    print(f"pre: missing passenger count: {df['passenger_count'].isna().sum()}")
    df['passenger_count'].fillna(0,inplace=True)
    print(f"post: missing passenger count: {df['passenger_count'].isna().sum()}")
    return df

@task()
def write_bq(df: pd.DataFrame) -> None:
    """Write Dataframe to Big Query"""
    gcp_credentials_block = GcpCredentials.load("prefect-gcp-creds")

    df.to_gbq(
        destination_table="taxi.rides",
        project_id="prefect-de-394505",
        credentials=gcp_credentials_block.get_credentials_from_service_account(),
        chunksize=200_000,
        if_exists="append"
    )

@flow()
def etl_gcs_to_bq():
    """Mian Etl flow to load data into Big query"""
    color = "yellow"
    year = 2021
    month = 1
    
    path = extract_from_gcs(color, year, month)
    df =transform(path)
    write_bq(df)

if __name__ == "__main__":
    etl_gcs_to_bq()