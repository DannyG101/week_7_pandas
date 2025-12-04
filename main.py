

if __name__ == "__main__":
    import utils

    #import JSON file and create a DataFrame
    df = utils.load_json("orders_simple.json")

    #Change total_amount to a Float
    df = utils.change_datatype_to_float(df)

    #Change order_date to datetime
    df = utils.change_datatype_to_datetime(df)

    #Remove HTML tags from items_html
    df = utils.remove_html_tags(df)

    #Replace empty spaces with NO COUPON in coupon_used
    df = utils.replace_empty_coupons(df)

    #create Order month column
    df = utils.create_order_month(df)

    #Create a new column to check if total is higher than average
    df = utils.create_high_value_order_row(df)

    #Sort table to be by total_amount descending
    df = utils.sort_df_by_total_amount(df)

    #Add column with country average rating
    utils.create_country_rating_average(df)

    #Filtering table to some conditions
    df = utils.filter_rows(df)

    #Create a new column with shipping status
    df = utils.add_delivery_status(df)

    #Save DataFrame as a CSV File
    utils.write_df_to_csv(df)


