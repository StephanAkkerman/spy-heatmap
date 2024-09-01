# S&P 500 Heatmap 📊

This project is a simple Python script that generates a heatmap of the S&P 500 index using the data from the Unusual Whales API. It is meant to look like the heatmap on the [Unusual Whales website](https://unusualwhales.com/heatmaps). You can save the heatmap as an image or open the dashboard to have a more detailed look into all the values.

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Supported versions">
  <img src="https://img.shields.io/github/license/StephanAkkerman/funding-rate-heatmap.svg?color=brightgreen" alt="License">
  <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black"></a>
</p>

---

## Introduction

If you have traded stocks you have probably come across the S&P 500 index and the heatmaps that are used to visualize the performance of the index. It provides a quick overview of the performance of the index and can be used to identify trends and patterns. Many sites provide these heatmaps, but I wanted to create my version using Python.

## Installation ⚙️

The required packages to run this code can be found in the requirements.txt file. To run this file, execute the following code block after cloning the repository:

```bash
pip install -r requirements.txt
```

## Usage ⌨️

To generate the chart, simply run the script using the following command:

```bash
python src/main.py
```

## Example 📊

The following chart is an example of the output generated by the script.
![SPY Heatmap](img/spy_heatmap.png)

### References 📚

The following image was used as a reference to create this heatmap.
![SPY Heatmap Ref](img/spy_heatmap_reference.png)

## Other Projects 📦

This project is part of a series of projects that I have created. You can find the other projects in the following list:

- [Total Liquidation Chart](https://github.com/StephanAkkerman/liquidations-chart)
- [Bitcoin Rainbow Chart](https://github.com/StephanAkkerman/bitcoin-rainbow-chart)
- [Live Binance Charts](https://github.com/StephanAkkerman/live-binance-charts)
- [RSI Heatmap](https://github.com/StephanAkkerman/crypto-rsi-heatmap)
- [Funding Rate Heatmap](https://github.com/StephanAkkerman/funding-rate-heatmap)
