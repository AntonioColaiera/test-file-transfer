import os
import random

# Function to create a folder
def create_folder(folder_name):
    # Check if the folder already exists
    if os.path.exists(folder_name):
        print(f"The folder '{folder_name}' already exists.")
    else:
        # Create the folder
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' successfully created.")

# Function to create subfolders for a given main folder
def create_subfolders(main_folder, start_year, number_of_subfolders):
    # Create the random number of subfolders
    for i in range(number_of_subfolders):
        # Each subfolder is named as a year, starting from the start_year and going backwards
        subfolder_name = str(start_year - i)
        subfolder_path = os.path.join(main_folder, subfolder_name)
        create_folder(subfolder_path)
        # Create files in the subfolder
        create_files(subfolder_path, year=subfolder_name)

# Function to create dummy files in a given folder
def create_files(folder_path, year):
    # Define the months and the number of days in each month
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Decide the number of files to create
    number_of_files = random.randint(1, 40)
    for i in range(number_of_files):
        # Generate a random month and day for the file name
        month_index = random.randint(0, 11)
        month = months[month_index]
        day = random.randint(1, days_in_month[month_index])
        # Create the file name
        file_name = f"{year}_{month_index+1:02d}_{day:02d}.wav"
        file_path = os.path.join(folder_path, file_name)
        # Create the file and write random data into it
        with open(file_path, 'wb') as f:
            # The file size is a random value between 1.1MB and 5MB
            f.write(os.urandom(int(1024 * 1024 * (1.1 + random.random() * (5 - 1.1)))))

# Main function
if __name__ == "__main__":
    # Define the main folder name and the start year
    main_folder_name = "Days with noise pollution in Milan"
    start_year = 2023
    # Decide the number of subfolders to create
    number_of_subfolders = random.randint(1, 25)
    # Create the main folder
    create_folder(main_folder_name)
    # Create the subfolders and the files in them
    create_subfolders(main_folder_name, start_year, number_of_subfolders)
