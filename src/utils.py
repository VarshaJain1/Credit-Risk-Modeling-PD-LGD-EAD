{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "id": "7ZfE7rd7AjRd"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "\n",
        "def load_csv_prices(path: str) -> pd.DataFrame:\n",
        "    df = pd.read_csv(path, index_col=0, parse_dates=True)\n",
        "    return df.sort_index()\n",
        "\n",
        "def example_weights(n_assets: int) -> np.ndarray:\n",
        "    w = np.ones(n_assets) / n_assets\n",
        "    return w"
      ]
    }
  ]
}
