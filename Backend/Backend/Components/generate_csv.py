import pandas as pd
from calendar import monthrange
from datetime import datetime

def create_status_csv(input_csv, month_name):
    # Load existing CSV file with "Email" column
    data = pd.read_csv(input_csv)

    # Extract unique email addresses
    email_list = data['Email'].unique()

    # Get the current year and month
    current_date = datetime.now()
    year, month = current_date.year, current_date.month

    # Get the number of days in the current month
    _, last_day = monthrange(year, month)

    # Create a DataFrame with "Email" column and date columns
    date_columns = [f"{day} {month_name} {year}" for day in range(1, last_day + 1)]
    status_df = pd.DataFrame(index=email_list, columns=['Email'] + date_columns)
    status_df['Email'] = email_list

    # Initialize each cell in date columns with the specified dictionary
    default_dict = {"Collection status": "No", "Points": 0, "Time": "00:00"}
    for col in date_columns:
        status_df[col] = [default_dict.copy() for _ in range(len(email_list))]

    # Save the DataFrame to a CSV file
    output_csv = f"{month_name}_status.csv"
    status_df.to_csv(output_csv, index=False)
    print(f"CSV file '{output_csv}' has been created successfully.")

# Example usage: Assuming you have an existing CSV file named 'input_data.csv'
input_csv_file = r"C:\Users\jeyashri.r\Downloads\WMS\Backend\Resource\Register.csv"
month_name = datetime.now().strftime("%B")  # Get the current month name
create_status_csv(input_csv_file, month_name)
