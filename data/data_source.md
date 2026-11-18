# Data Source

## Dataset Information

**Dataset:** Annual Temperature Anomalies  
**Provider:** Our World in Data  
**Source URL:** https://ourworldindata.org/grapher/annual-temperature-anomalies.csv?v=1&csvType=full&useColumnShortNames=false

## Description

The dataset contains annual temperature anomaly measurements for countries and geographical regions.

The analysis focuses on records identified as `World`, covering the period from 1940 to 2025.

## Data Fields

| Column | Description |
|---|---|
| Entity | Country or geographical region |
| Code | Country or region identifier |
| Year | Observation year |
| Temperature anomaly | Annual temperature anomaly |

## Data Processing

The original dataset was loaded using Pandas. The global records were selected by filtering the `Entity` column for `World`.

Missing values were inspected in the original dataset and in the filtered global dataset.

The selected global dataset contains 86 records and no missing values.

## Usage

The dataset is used for statistical analysis and visualisation of long-term global temperature anomaly trends.