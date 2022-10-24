# ImputeGAN: Generative Adversarial Network for Multivariate Time Series Imputation
## Requirements
- Python 3.6
- matplotlib == 3.1.1
- numpy == 1.19.4
- pandas == 0.25.1
- scikit_learn == 0.21.3
- torch == 1.8.0
## Data
The dataset for the experiment includes
- ETT(Electricity Eransformer Temperature): The ETT dataset contains two years of data on oil temperature of power transformers in two counties in China and six other metrics.
- KDD(KDD Cup 2018 Dataset): The KDD 2018 Cup dataset, which contains weather data and air pollution data collected by hour from January 30, 2017 to January 30, 2018 for Beijing and London.
- ECL(Electricity Consuming Load): The ECL dataset contains electricity consumption data for 321 clients for the years 2012 to 2014.
- Weather(Weather Dataset): TThe Weather dataset contains weather data collected hourly from 2010 to 2013 for 1600 locations in the United States.

All of these datasets and their corresponding missing 10% to 80% of files are in the /data/ETT directory
## Usage
Commands to test the imputation

`python -u main_informer.py --model informer --data ETTh1 --do_predict --pred_len 24 --seq_len 48 --label_len 24 --itr 2`

The detailed descriptions about the arguments are as following:
| Parameter name    | Description of parameter |
| ----------- | ----------- |
| data      | The dataset name       |
| do_predict   | Whether to impute missing data, using this argument means making imputations |
| pred_len | Imputation sequence length |
| seq_len | Input sequence length of auto-encoder encoder |
| label_len | Start token length of auto-encoder decoder |
| itr | Experiments times |

To change the dataset miss ratio, specify the dataset file by changing Data_Imputation in data_loader.py
