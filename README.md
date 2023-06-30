# BankListAPI

I am using Django REST Framework for achieving endpoints given in assignment.

![RootAPI](https://github.com/Kkanu17/BankListAPI/blob/main/ImageFolder/RootAPI.png)

Requirements:
•	Python
•	Django
•	Django REST Framework
•	MySql

REST API endpoints have been created, by requesting the URL we get:-
•	GET Bank List : This gives us bank name and its id

![BankListAPI](https://github.com/Kkanu17/BankListAPI/blob/main/ImageFolder/BankListAPI.png)


•	GET Branch details : This gives us branch details along with bank name its fields are ifsc, bank name, branch name,  address, city, District, state.

![BranchListAPI](https://github.com/Kkanu17/BankListAPI/blob/main/ImageFolder/BranchListAPI.png)

If we want to fetch Bank List and Branch details for specific Branch we can fetch it by 
Example:  /branch=? NEW PANVEL

![PostmanBranchListGetRequestFilter](https://github.com/Kkanu17/BankListAPI/blob/main/ImageFolder/PostmanBranchListGetRequestFilter.png)



I am using bank_branches.csv and indain_banks.sql files for Database given in repository. I have inserted the above given data into MySql by using the insert statement.

Note: Form MySql database settings, I have used root user and created a new database name: djangodb
Further details of database connection can be found the django settings.py file.
I have provided SessionAuthentication with the IsAuthentecatedOrReadOnly permission class by which anyone can see details using this API but cannot post it until it is authorized. 
I have used Postman to test API and checking for Test Cases. Test cases file is attached.
