import pandas as pd

def transform_data():
    input_path = '/tmp/sales_data.csv'
    output_path = '/tmp/sales_data_transformed.csv'

    df = pd.read_csv(input_path, encoding="latin1")

    df = df.dropna()
    df['order_date'] = pd.to_datetime(df['ORDERDATE'])

    agg_df = df.groupby('PRODUCTLINE').agg(
        total_sales=('SALES', 'sum'),
        total_orders=('ORDERNUMBER', 'nunique')  # unique orders
    ).reset_index()

    agg_df.to_csv(output_path, index=False)
    print(f"Transformed data saved to {output_path}")