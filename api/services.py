import pandas as pd
import os
from django.conf import settings


def load_sales_data():
    base_dir = settings.BASE_DIR

    csv_path = os.path.join(base_dir, "dataset", "sales.csv")

    df = pd.read_csv(csv_path)

    return df
