import pandas as pd


def load_json(path:str):
    return pd.read_json(path)


def change_datatype_to_float(dataframe):
    dataframe.total_amount =  pd.to_numeric(dataframe.total_amount.str.replace('$', ''))
    return dataframe

def change_datatype_to_datetime(dataframe):
    dataframe.order_date =  pd.to_datetime(dataframe.order_date)
    return dataframe

def remove_html_tags(dataframe):
    dataframe.items_html.str.replace("<.*?>", " ", regex=True).str.strip()
    return dataframe

def replace_empty_coupons(dataframe):
    dataframe.coupon_used = dataframe.coupon_used.replace("", "NO COUPON")
    return dataframe

def create_order_month(dataframe):
    return dataframe.assign(order_month=dataframe.order_date.dt.month)

def create_high_value_order_row(dataframe):
    average_amount = dataframe["total_amount"].mean()
    return dataframe.assign(high_value_order=lambda x: x.total_amount >= average_amount)


def sort_df_by_total_amount(dataframe):
    return dataframe.sort_values("total_amount", ascending=False)


def create_country_rating_average(dataframe):
    dataframe["country average"] = dataframe.groupby("country")["rating"].transform("mean")
    return dataframe


def filter_rows(dataframe):
     return dataframe[(dataframe["total_amount"] > 1000) & (dataframe["rating"] > 4.5)]

def time_check(shipping_days):
    if shipping_days > 7:
        return "delayed"
    else:
        return "on time"

def add_delivery_status(dataframe):
    return dataframe.assign(delivery_status = lambda x: x.shipping_days.apply(time_check))


def write_df_to_csv(df):
    df.to_csv("clean_orders_[ID_NUMBER].csv")
