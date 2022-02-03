
#  Imports
import os
import csv  

#  if your working system does not have Pretty Table use "$ sudo pip3 install PTable" to install
from prettytable import PrettyTable 






##################
#  DISPLAY CSV
##################
def Table_display(path, filename):
    #To display the csv file. 
    Fullpath = os.path.join(path, filename)
    print(Fullpath, "\n")

    x = PrettyTable()


    rows = []
    with open(Fullpath, 'r') as file:
        csvreader = csv.reader(file)
        x.field_names = next(csvreader)

        for row in csvreader:
          x.add_row(row)

    print(x)


#######################################
#  COMBINING THE SELECTED CSV FILES
#######################################
def combiner(fixtures_path, files_to_combine):
    # Code to combine the .csv file
    data = []
    counter = 1

    for csv_file in files_to_combine:
    
        print(csv_file)  
        with open(os.path.join(fixtures_path, csv_file), 'r') as f:
           
             reader = csv.reader(f)
             row = next(reader)
  
             if(counter == 1):
                row.append('filename')
                data.append(row)
                counter+=1
       

             for row in reader:
                row.append(csv_file)
                print(row)
                data.append(row)

    # print(data)
    len(data)
    # type(data)
    return data
        


#######################################
#  SAVING NEW CSV FILES
#######################################
def save_to_csv(Output_Path, Output_filename, data):
    # saving the combined csv
    with open(os.path.join(Output_Path, Output_filename), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)   






def main(fixtures_path):
 
    selected_lst = []
    # displaying files for the user.
    print("List of . csv files in the directory")
    ListOfFiles = os.listdir(fixtures_path)
    print(ListOfFiles, "\n")

   

    for index, value in enumerate(ListOfFiles):
      print(index, value)
    
    print("\n")

    # reading user inputs
    NumbOfFiles = int(input("Enter the number of files you want to combine:\n"))

    for i in range(0, NumbOfFiles):
      print("Select csv:",i+1," to combine - \n")
      user_input = int(input())
      selected_lst.append(ListOfFiles[user_input])
    print(selected_lst,"\n")

    return selected_lst


if __name__ == "__main__":

    path_input = input(" Copy and past the relative path of CSV combiner folder in your system:\n example: C:\zahid\PNG\Coding task\CSV combiner \n ")
    fixtures_path = os.path.join(path_input,'fixtures')
    print(fixtures_path,"\n")

    Output_Path = os.path.join(path_input,'Output')
    print(Output_Path,"\n")

    

    files_to_combine = main(fixtures_path)

 
    # Printing the tables
    print("Files selected to combine:- \n")
    for index, csv_file in enumerate(files_to_combine):
        print("file no.", index+1, "\n")
        print(csv_file,"\n")
        Table_display(fixtures_path, csv_file)
        print("\n")
     
    #  Combining the files
    data = combiner(fixtures_path, files_to_combine)

    #  saving the csv file
    Output_filename = input ("Name the new .csv file:")
    print(Output_filename, " file was created in Output folder! \n")
    save_to_csv(Output_Path,Output_filename, data)


    print("Csv combining complete!! \n")
    
    
    
    print("Output files after combining:- \n")
    Table_display(Output_Path, Output_filename)
