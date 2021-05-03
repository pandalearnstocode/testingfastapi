# MLOps & DevOps
0. Check idle timeout for ACI
1. Split TF code --> Create a dummy python package
2. Control dynamics layers by country, commit hash, python package version and use data from pyexample
3. Create two separate requirements for CPU and GPU
4. Create two difference package tags pyexample[cpu] & pyexample[gpu]
5. Automated testing using GPU on code change in github via GitHub action
6. Create a release pipeline, code change --> package build --> push to Azure DevOps
7. Publish package to Azure DevOps as artifact
8. Create a docker image from pulling the package from azure devops artifact
9. Publish docker image to acr with a tag
10. Install Sonar Cloud & security scanning
11. Generate & publish wily report
12. Test coverage report generate and publish
13. Python library docs generate and publish



# Data
1. POS Data -- BI team
2. Media Data -- BI team
3. Weather Data -- BI team
4. Holidays Data -- BI team
5. Macro-economics Data -- BI team
6. Financial and shipment Data -- BI team
7. Power Data -- BI team (Check power data usage. Data from BI team and zone is different)
8. ROI Warehouse Data  -- GAC
9. ROI Curves Data  -- GAC
10. Response Curves Data  -- GAC


1. For all the data sources get 10000 rows, save in a parquet file and upload in a drive folder.
2. Create code to generate the same files for country level.
3. Generate headers and send
4. Data types
5. List steps we are performing to each dataset currently (BI source --> AML Blob)
